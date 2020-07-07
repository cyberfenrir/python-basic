import urllib.request, urllib.parse, urllib.error
#import BeautifulSoup
import ssl
import re

#ssl error rectification
ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

summation= 0
url= input("enter url: ")
html = urllib.request.urlopen(url, context=ctx)
for line in html:
	line = line.decode()
	z=line.rstrip()
	y = re.findall("[0-9]+",z)
	if (len(y)<1):
		continue
	#print(y)
	for x in y:
	 	x= int(x)
	 	summation = summation + x 
print(summation-8)