inputString = input("Enter space separated ints: ").split(" ")

boolString = []
for i in inputString:
	boolString.append(str(bin(int(i))).split("b")[1])		#Converts Python's binary format into normal binary

checkArray = [0 for i in range(10)]
insertedList = []

for i in boolString:
	reverseStr = i[::-1]
	hash1 = int(reverseStr[0::2],2)%10		#Hash of converted odd binary bits modded by any number (10 in this case)
	hash2 = int(reverseStr[1::2],2)%10		#Hash of converted even binary bits modded by any number (10 in this case)
	if(checkArray[hash1]==checkArray[hash2] and checkArray[hash1] == 1):			
		if i in insertedList:			
			print("Collision!")
		else:
			print("False positive! No collision!")
			insertedList.append(i)
			checkArray[hash1] = 1
			checkArray[hash2] = 1
	else:
		print("No collision!")
		insertedList.append(i)
		checkArray[hash1] = 1
		checkArray[hash2] = 1


