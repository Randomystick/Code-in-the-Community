import random

while True: #input validation for length of list | True needs to be capitalised
    try:
        listLength = int(input("Please enter the length for the list: "))
    except ValueError:
        print("Error: Enter an INTEGER")
        continue
    if listLength < 0:
        print("Error: Length must be POSITIVE (more than 0)")
        continue
    else:
        break

def listPrint(LowerorUpper): #obtain bounds via function to save on retyping text
    print("Please enter the " + LowerorUpper + " bound for the range of integer values: ", end="") #the end="" prevents going to newline - it's a python thing
    listNumber = int(input())
    return listNumber
listLower = listPrint("lower")
listUpper = listPrint("upper")

listofNo = [None] * listLength #initialise array (called list in Python) of appropriate size
print("Sequence: [", end="")
for i in range(listLength):
    listofNo[i] = random.randint(listLower, listUpper)
    print(listofNo[i], end ="")
    if i == (listLength-1):
        break #skip printing the comma after the last number
    print(", ", end ="")
print("]")

print("List length:", listLength)

listMax = listLower #ensure that listMax is guaranteed to adopt a value from the list by making the "if" condition true at least once
for i in range(listLength):
    if listMax < listofNo[i]: 
        listMax = listofNo[i]
print("Largest integer:", listMax)

listMin = listUpper #same concept as listMax
for i in range(listLength):
    if listMin > listofNo[i]: 
        listMin = listofNo[i]
print("Smallest integer:", listMin)

listSum = 0
for i in range(listLength):
    listSum += listofNo[i]
print("Sum:", listSum)

print("Average:", listSum / listLength)


#endfile