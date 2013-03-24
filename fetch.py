import pnrapi
p = pnrapi.PNRAPI("1234567890") #10-digit PNR Number
if p.request() == True:
	print p.get_json()
else:
	print "Service unavailable"
