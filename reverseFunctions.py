#Some of my first functions
#Reverse a List or a String using concatenation (my favorite method so far)

text="My country 'tis of thee!"

textList = text.split(" ")#turn string into a List
print (textList)


myList = [1,12,24,"sing",42,56,73,89,99,201,101]
l = myList[:] #make a copy of original list
print (l)

#reverseList
#Takes a list and reverses it
#using concatenation
def reverseList(myList):
	newList = []
	for i in range (len(myList)):
		addList=[myList[i]]
		newList = addList + newList
	return (newList)
#reverseString
#Takes a string and reverses it
#using concatenation
def reverseString(myString):
	newString = ""
	for i in range (len(myString)):
		newString = myString[i]+newString
	return (newString)
	
l = reverseList(l)
print (l)

newTextList = reverseList(textList)
print (newTextList)

newTextString=" ".join(new)
print (newTextString)

print (text)
reverseText = reverseString(text)
print (reverseText)
