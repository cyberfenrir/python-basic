import re
import urllib.request, urllib.parse, urllib.error
import ssl
#import bs4
from bs4 import BeautifulSoup
import socket


#ssl certifying error rectification
ctx= ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def function(url):
    count= 0
    html = urllib.request.urlopen(url, context=ctx)
    soup = BeautifulSoup(html,"html.parser")

    #retrieval of anchor tags
    tags = soup('a')
    for tag in tags:
        #x=tag.get('href', None)
        print(tag.get('href', None))
        count=count+1
        z= tags.index(tag)
    if z==17:
        url = tags[z]
    #print(count)
    #print(name)'
    print("\n")
    return(url)

name = input("Enter the url: ")
limit = int(input("enter the limit: "))
i=0
while(i<limit):
    y=function(name)
    print(y," ")
    name=y
    print(name,)
    i=i+1
print("the last name is: ", name)
