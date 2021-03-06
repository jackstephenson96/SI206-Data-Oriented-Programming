import os
import datetime
from datetime import date
import csv
import filecmp

def getData(file):
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	dic = {}
	data = []
	fil = open(file, "r")
	firstLine = fil.readline().split(",")
	for line in fil.readlines():
		dic[firstLine[0]] = line.split(",")[0]
		dic[firstLine[1]] = line.split(",")[1]
		dic[firstLine[2]] = line.split(",")[2]
		dic[firstLine[3]] = line.split(",")[3]
		dic[firstLine[4]] = line.split(",")[4]
		data.append(dic)
		dic = {}
	return data

#Sort based on key/column
def mySort(data, col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	top = sorted(data, key = lambda x: x[col])[0]
	return str(top["First"]) + " " + str(top["Last"])
 
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	senior, junior, sophomore, freshman = 0, 0, 0, 0
	returnList = []
	for dic in data:
		if dic["Class"] == "Senior":
			senior += 1
		if dic["Class"] == "Junior":
			junior += 1
		if dic["Class"] == "Sophomore":
			sophomore += 1
		if dic["Class"] == "Freshman":
			freshman += 1
		returnList = [("Senior", senior), ("Junior", junior), ("Sophomore", sophomore), ("Freshman", freshman)]
	return sorted(returnList, key = lambda x: x[1], reverse=True)
	



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	days = {}
	for dic in a:
		day = int(dic["DOB\n"].split("/")[1])
		if day not in days:
			days[day] = 1
		else:
			days[day] += 1
	topDay = sorted(days, key=days.get, reverse=True)[0]
	return(topDay)



# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	total = 0
	avg = 0
	i = 0
	for dic in a:
		born = datetime.datetime.strptime(dic["DOB\n"].strip(), "%m/%d/%Y").date()
		today = date.today()
		age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
		total = total + int(age)
		i = i + 1
	avg = total / i
	return int(round(avg))



#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	fileString = str(fileName)
	data = sorted(a, key = lambda x: x[col])
	with open(fileString, "a") as outfile:
		if os.stat(fileString).st_size == 0:
			for dic in data:
				outfile.write("{},{},{},\n".format(dic["First"], dic["Last"], dic["Email"]))
					












################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()


