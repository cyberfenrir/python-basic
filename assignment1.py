import re
filename = input()
if(len(filename)==0):
	filename= "regex_sum_691845.txt"
handle=filename.open()
for line in handle:
	print(line)