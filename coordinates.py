import urllib.request, urllib.parse, urllib.error
import json

#service url
surl = "https://maps.googleapis.com/maps/api/geocode/json?"
while True:
	address = input("enter the address(the name of the place with state): ")
	if len(address)<1:
		break
	url = surl + urllib.parse.urlencode({'address': address})
	print('retrieving', url)
	uh=urllib.request.urlopen(url)
	data= uh.read().decode()
	print('retrieved ', len(data),' characters')
	try:
		js=json.loads(data)
	except:
		js=None
	if not js or 'status' not in js or js['status'] != 'OK':
		print('==== FAILED TO RETRIEVE DATA ====')
		print(data)
		continue
	lat=js['results'][0]['geometry']['location']['lat']
	lng=js['results'][0]['geometry']['location']['lng']
	location = js['results'][0]['geometry']['location']
	print(location)
	print('lat:',lat,"long: ",lng)