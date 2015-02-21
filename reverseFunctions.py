#reverse a list with concatenation

text="My country 'tis of thee!"
textList = text.split(" ")
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
	
def reverseString(myString):
	newString = ""
	for i in range (len(myString)):
		newString = myString[i]+newString
	return (newString)
	
l = reverseList(l)
print (l)

new = reverseList(textList)
print (new)

newText=" ".join(new)
print (newText)

print (text)
reverseText = reverseString(text)
print (reverseText)
