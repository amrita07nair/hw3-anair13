import time
import math
import csv
import tempfile
def hw3_Q1FizzBuzz():
	#ive dont stuff like this in python before so this was good. I had to look up the syntax for time and range() because if was rusty on it but i knew how to program this in python and java
	timestart=time.time()
	for i in range(1,101,1):
		if i%3==0 and not i%5==0:
			print("Fizz")
		elif i%5==0 and not i%3==0:
			print("Buzz")
		elif i%5==0 and i%3==0:
			print("FizzBuzz")
		else:
			print(i)
	timeend=time.time()
	totaltime=timeend-timestart
	print("It took ", totaltime,"seconds to do FizzBuzz.")

def hw3_Q2VolumeofSphere():
	#this was also something i was familiar with doing. I had a small issue wit casting the input to an int. I forgot that it was not like java where it would be like radius = int()input() or trying to cast in the volume var. So that i had to look at the syntax for but this was straight forward.
	print("Enter the radius of the sphere you would like to find the volume of. ")
	radius = int(input())
	volume = (4/3)*(math.pi)*(radius**3)#I knew there was a better way for doing the radius^3 i know there is a pow function and an operator way. but had trouble remembering the exact syntax so i had to look that up and remembered it is base**exponent. I took cis intro to programming and learned the basics of python but it had been many months and i forgot some syntax and little things.
	#print((4/3)*(math.pi)*(radius*radius*radius))
	print("The volume of the sphere of radius ", radius, "is ", volume)


def hw3_Q3MakeWriteCSVFileFromDictionary():
	#I have never done any work in python with CSVs or files. 
	#I had many iterations of code and this was the one that works. I knew the basic procedures from System level programming where you have to get the file, read the contents, and then write. so i kind of knew how to do this but did not know the specifics of csv and python syntax. I did it with C and only regular files, so i had to figure out the CSV and python part. 
	#I dont have any experience dealing with CSVs even in python, so i had to use some reference material
	#I had many iterations of code and did my best to only look up syntax and certain small errors. 
	#I have never in any language used a dictionary, so again i had to look at the procedures from that but it reminded me of arrays in an array in java but mapped to column names. 
	#print("Q3")
	fieldname_columns = ["Title", "Author", "ISBN", "No. Pages"] #feildnames for the data
	dictionary=[
		{"Title":"1984","Author":"George Orwell","ISBN":"978-0451524935","No. Pages":268},
		{"Title":"Animal Farm","Author":"George Orwell","ISBN":"978-0451526342","No. Pages":144},{"Title":"Brave New World","Author":"Aldous Huxley","ISBN":"978-0060929879","No. Pages":288},{"Author":"Fahrenheit 451","Title":"Ray Bradbury","ISBN":"978-0345342966","No. Pages":208}
		]#the fieldnames must be exact so that they are written properly or there is an error. I tested out changing the order up too with the last entry.
	#print(dictionary)
	with open('booksDictionary.csv','w')as csvfile:#open a new file named ' ' and w means we are going to write in the empty file
		writer = csv.DictWriter(csvfile, fieldnames=fieldname_columns)#we make a writer variable and are going to use dictwriter because that is what we want to write 
		writer.writeheader()# write the feildnames at the top
		writer.writerows(dictionary)#write the rows from the dictionary as they match to the feilds **note the test for the last entry

def hw3_Q4ReturnDictionaryfromCSVFile():
	#as i explained in q3 i have little experience with files and
	#I kept only getting one line from the file, so i know i needed a for loop but did not know the correct way to do it. 
	#print("Q4")
	dictionary=[]#initialize the empty dictionary that will be filled from the csv
	getCSVfile = open('booksDictionary.csv', 'r')#step 1: use a variable to open the file named "" and r stands for read. 
	readCSVasDict = csv.DictReader(getCSVfile)#step 2: use dictreader to read the csvfile data from getcsv but read it like a dictionary would
	for rows in readCSVasDict:#for the rows of data in the dictionaryread version of the csv, append the rows to the empty dictionary (because we are going line by line from row 0 to the end, the data will be added to the dictionary in the correct order)
		dictionary.append(rows)
	print(dictionary)
def hw3_Q5Combine3and4UseTempFiles():
	#now i have q3 and q4, so now i have to figure out temp files. I am using the link provided, but I have never in any language or class used temp files. 
	#since i am combining my q3 and q4 for q5, i copied and pasted that work here to then edit for temp files
	fieldname_columns = ["Title", "Author", "ISBN", "No. Pages"]
	dictionaryfromq3=[
		{"Title":"1984","Author":"George Orwell","ISBN":"978-0451524935","No. Pages":268},
		{"Title":"Animal Farm","Author":"George Orwell","ISBN":"978-0451526342","No. Pages":144},{"Title":"Brave New World","Author":"Aldous Huxley","ISBN":"978-0060929879","No. Pages":288},{"Author":"Fahrenheit 451","Title":"Ray Bradbury","ISBN":"978-0345342966","No. Pages":208}
		]
	temporaryfile = tempfile.TemporaryFile()
	with open('temporaryfile.csv','w')as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldname_columns)
		writer.writeheader()
		writer.writerows(dictionaryfromq3)
	dictionaryfromq4=[]
	getCSVfile = open('temporaryfile.csv', 'r') 
	readCSVasDict = csv.DictReader(getCSVfile)
	for rows in readCSVasDict:
		dictionaryfromq4.append(rows)
	print("here")
	#temporaryfile.delete()

hw3_Q1FizzBuzz()
hw3_Q2VolumeofSphere()
hw3_Q3MakeWriteCSVFileFromDictionary()
hw3_Q4ReturnDictionaryfromCSVFile()
hw3_Q5Combine3and4UseTempFiles()