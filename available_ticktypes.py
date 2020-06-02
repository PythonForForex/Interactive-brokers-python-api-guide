from ibapi.ticktype import TickTypeEnum

for i in range(91):
	print(TickTypeEnum.to_str(i), i)