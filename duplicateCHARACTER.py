#Write a program that takes a string as input and returns the first duplicate character."

string = "The quick brown fox jumped over the lazy dog."

#My first idea is to make an array of boxes that hold each character
#Before placing a character in the box, check that the box is empty
#If the box is full, that is the first duplicate character

#Don't know how to make an array of boxes big enough for each character 
#and then append the value of the character to the index of that box
#ord() is used to get the ascii value for a character
#how to put that value into that index of the array?

#~ boxes = []
#~ for item in string:
	#~ 
	#~ boxes.append(ord(item))
	#~ 
	#~ print (item)
#~ print (boxes)

#Another idea is to take the first character and search the rest of the 
#string for it, and so on
#Except this method doesn't really do that
#what this does is find the first location of a character in the string
#and map it to an array
#If the location of the character is less than the length of the array, it
#has already been found and so it is a duplicate

collection=[]
for character in string:
	result = string.find(character) + 1 #add 1 so index is the same as length of array
	collection.append(result)
	print (character)
	#print ("length of collection", len(collection))
	#print ("Place found", result)
	
	if result < len(collection):
		print ('A DUPLICATE CHARACTER HAS BEEN FOUND!')
		print ('The duplicate is: "%s"'  % character)
		#print ()
			
#print (collection)

#print ("Third idea")

#Use something similar to this Hamming Distance algorithm

#~ length = len(string)
#~ for x in range(0, length):
	#~ character1 = text1[x]
	#~ character2 = text2[x]
	#~ print("1 is", character1, "2 is", character2)
	#~ if character1 != character2:
		#~ distance=distance +1
#~ 
#~ print ("distance is", distance)
