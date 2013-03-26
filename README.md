pnrapi-python
=============

A Python web-scraper for Indian Railways' PNR Status.

Requirements
------------
* [Beautiful Soup 4][1]
  - `pip install beautifulsoup4` or `easy_install beautifulsoup4`
* [Requests][2]
  - `pip install requests` or `easy_install requests`

Sample Request
--------------
	import pnrapi
	p = pnrapi.PNRAPI("1234567890") #10-digit PNR Number
	if p.request() == True:
		response = p.get_json()
		print response
	else:
		print "Service unavailable"

Sample Response
---------------
The reponse is a json object as follows:

	{
		'pnr': '1234567890',
		'ticket_type': 'E - TICKET',
		'train_number': '12230'
		'train_name': 'LUCKNOW MAIL',
		'boarding_date': '14-3-2013',
		'from': 'NDLS',
		'to': 'LKO',
		'reserved_upto': 'LKO',
		'boarding_point': 'NDLS',
		'class': '3A',
		'total_passengers': 1,
		'charting_status': 'CHART PREPARED',
		'passenger_status': [
			{'booking_status': 'W/L 10,GNWL', 'current_status': 'B4 , 17'}
		]
	}
The `passenger_status` array will contain `total_passengers` number of elements.


[1]: http://www.crummy.com/software/BeautifulSoup/
[2]: https://github.com/kennethreitz/requests
