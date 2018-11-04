import re
total, number = 0, 0
f = open("realdata.txt" , "r")
for line in f:
	num = re.findall("[0-9]+", line)
	for i in num:
		number = number + int(i)
	total = total + number
	number = 0
print(total)