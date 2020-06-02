from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time


class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
		
	def tickPrice(self, reqId, tickType, price, attrib):
		if tickType == 2 and reqId == 1:
			print('The current ask price is: ', price)

def run_loop():
	app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 123)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
BTC_futures__contract = Contract()
BTC_futures__contract.symbol = 'BRR'
BTC_futures__contract.secType = 'FUT'
BTC_futures__contract.exchange = 'CMECRYPTO'
BTC_futures__contract.lastTradeDateOrContractMonth  = '202003'

#Request Market Data
app.reqMktData(1, BTC_futures__contract, '', False, False, [])

time.sleep(10) #Sleep interval to allow time for incoming price data
app.disconnect()