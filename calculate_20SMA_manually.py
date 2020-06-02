from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract

import threading
import time

class IBapi(EWrapper, EClient):
	def __init__(self):
		EClient.__init__(self, self)
		self.data = [] #Initialize variable to store candle

	def historicalData(self, reqId, bar):
		print(f'Time: {bar.date} Close: {bar.close}')
		self.data.append([bar.date, bar.close])
		
def run_loop():
	app.run()

app = IBapi()
app.connect('127.0.0.1', 7497, 126)

#Start the socket in a thread
api_thread = threading.Thread(target=run_loop, daemon=True)
api_thread.start()

time.sleep(1) #Sleep interval to allow time for connection to server

#Create contract object
eurusd_contract = Contract()
eurusd_contract.symbol = 'EUR'
eurusd_contract.secType = 'CASH'
eurusd_contract.exchange = 'IDEALPRO'
eurusd_contract.currency = 'USD'


#Request historical candles
app.reqHistoricalData(1, eurusd_contract, '', '2 D', '1 hour', 'MIDPOINT', 0, 1, False, [])

time.sleep(5) #sleep to allow enough time for data to be returned


### Calculate 20 SMA without a library
total = 0
for i in app.data[-20:]:  
    total += float(i[1])

print('20SMA =', round(total/20, 5)) 


app.disconnect()