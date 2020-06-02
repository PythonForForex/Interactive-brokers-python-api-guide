from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.order_condition import Create, OrderCondition
from ibapi.order import *

import threading
import time

class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
		self.contract_details = {} #Contract details will be stored here using reqId as a dictionary key

	def nextValidId(self, orderId: int):
		super().nextValidId(orderId)
		self.nextorderId = orderId
		print('The next valid order id is: ', self.nextorderId)

	def orderStatus(self, orderId, status, filled, remaining, avgFullPrice, permId, parentId, lastFillPrice, clientId, whyHeld, mktCapPrice):
		print('orderStatus - orderid:', orderId, 'status:', status, 'filled', filled, 'remaining', remaining, 'lastFillPrice', lastFillPrice)
	
	def openOrder(self, orderId, contract, order, orderState):
		print('openOrder id:', orderId, contract.symbol, contract.secType, '@', contract.exchange, ':', order.action, order.orderType, order.totalQuantity, orderState.status)

	def execDetails(self, reqId, contract, execution):
		print('Order Executed: ', reqId, contract.symbol, contract.secType, contract.currency, execution.execId, execution.orderId, execution.shares, execution.lastLiquidity)

	def contractDetails(self, reqId: int, contractDetails):
		self.contract_details[reqId] = contractDetails

	def get_contract_details(self, reqId, contract):
		self.contract_details[reqId] = None
		self.reqContractDetails(reqId, contract)
		#Error checking loop - breaks from loop once contract details are obtained
		for i in range(50):
			if not self.contract_details[reqId]:
				time.sleep(0.1)
			else:
				break
		#Raise if error checking loop count maxed out (contract details not obtained)
		if i == 49:
			raise Exception('error getting contract details')
		#Return contract details otherwise
		return app.contract_details[reqId].contract



def run_loop():
	app.run()

def Stock_contract(symbol, secType='STK', exchange='SMART', currency='USD'):
	''' custom function to create stock contract '''
	contract = Contract()
	contract.symbol = symbol
	contract.secType = secType
	contract.exchange = exchange
	contract.currency = currency
	return contract

app = IBapi()
app.connect('127.0.0.1', 7496, 123)

app.nextorderId = None

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

#Check if the API is connected via orderid
while True:
	if isinstance(app.nextorderId, int):
		print('connected')
		break
	else:
		print('waiting for connection')
		time.sleep(1)

#Create contracts
apple_contract = Stock_contract('AAPL')
google_contract = Stock_contract('GOOG')

#Update contract ID
google_contract = app.get_contract_details(101, google_contract)

##Create price conditions
#init
priceCondition = Create(OrderCondition.Price)
priceCondition.conId = google_contract.conId
priceCondition.exchange = google_contract.exchange

#create conditions
priceCondition.isMore = True
priceCondition.triggerMethod = priceCondition.TriggerMethodEnum.Last
priceCondition.price = 1400.00

#Create order object
order = Order()
order.action = 'BUY'
order.totalQuantity = 100
order.orderType = 'MKT'
#order.lmtPrice = '300' - optional - you can add a buy stop limit here
order.conditions.append(priceCondition)
order.transmit = True

app.placeOrder(app.nextorderId, apple_contract, order)

time.sleep(3)
app.disconnect()