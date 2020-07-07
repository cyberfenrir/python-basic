import re
filename = input("enter the name of the file: ")
if(len(filename)==0):
	filename= "regex_sum_691845.txt"
handle=open(filename)
summ=0
for line in handle:
	#print(line)
    line=line.rstrip()
    y= re.findall('[0-9]+',line)
    if(len(y)==0) :
    	continue
    #print(y)
    for x in y:
    	w = int(x)
    	summ=summ+w
print(summ)