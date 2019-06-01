print("TENKTUP1\n")
print("unique1 unique2 two four ten twenty onePercent tenPercent twentyPercent fiftyPercent unique3 evenOnePercent oddOnePercent stringu1 stringu2 string4\n")
#generate for loop for all tuples

import random

infile = open("onektup.txt","w")
def string4Generator(intInput):
	case = intInput % 4
	if case == 0: 
		return "AAAAxxx..."
	elif case == 1:
		return "HHHHxxx..."
	elif case == 2:
		return "OOOOxxx..."
	else: #case == 3:
		return "VVVVxxx..."

def uniqueConverter(intInput):
	counter =  intInput
	temp = "AAAAAAA"
	i = 6
	resultString = ""
	while i >= 0 and counter > 0:
		rem = counter % 26
		charAdd = chr(ord(temp[i]) + rem)
		counter = counter / 26
		resultString = charAdd + resultString
		--i
	length = len(resultString)
	length = 7 - length
	for x in range(length):
		resultString = 'A' + resultString
	resultString = resultString + "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
	return resultString

MAXTUPLES = 1000
randList = random.sample(xrange(MAXTUPLES),MAXTUPLES)

start = 0
while start < MAXTUPLES:
	unique1 = randList[start] #first tuples 0 - (Maxtuples - 1) random
	unique2 = start #second tuples 0 - (Maxtuples - 1) cyclic
	two = unique1 % 2
	four = unique1 % 4
	ten = unique1 % 10
	twenty = unique1 % 20
	onePercent = unique1 % 100
	tenPercent = unique1 % 10
	twentyPercent = unique1 % 5
	fiftyPercent = unique1 % 2
	unique3 = unique1
	evenOnePercent = onePercent * 2
	oddOnePercent = onePercent * 2 + 1
	stringu1 = uniqueConverter(unique1) # some function1
	stringu2 = uniqueConverter(unique2)# some function2
	string4 = string4Generator(start)
#print("%d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d",unique1,unique2,two,four,ten,twenty,onePercent,tenPercent,fiftyPercent,unique3,evenOnePercent, oddOnePercent)

	#print unique1,",",unique2,",",two,",",four,",",ten,",",twenty,",",onePercent,",",tenPercent,",",twentyPercent,",",fiftyPercent,",",unique3,",",evenOnePercent,",",oddOnePercent,",",stringu1,",",stringu2,",",string4
	infile.write("%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%i,%s,%s,%s\n" % (unique1,unique2,two,four,ten,twenty,onePercent,tenPercent,twentyPercent,fiftyPercent,unique3,evenOnePercent,oddOnePercent,stringu1,stringu2,string4))
	start += 1
infile.close()
