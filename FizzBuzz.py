#Loop through integers and print "Fizz" if it's divisible by 3
#Print "Buzz" if it's divisible by 5

counter = 0

while counter < 20:
	if counter % 5 == 0 and counter % 3 == 0:
		print ("FizzBuzz ")
	elif counter % 3 == 0:
		print ("Fizz ")
	elif counter % 5 == 0:
		print ("Buzz ")
	counter += 1
	#print("counter", counter)
	
	if counter >20:
		break
		
#try it with string concatenation zz="Fizz" zz+="Buzz" print(counter, zz)
print ()
print 
print ("using concatenation of strings")
print		
index = 0
zz = ""

#print ("index", index)

while index < 20:
    zz="Fizz"
    if index % 3 == 0 and index % 5==0:
        zz += "Buzz"
        print (zz)
    elif index % 3 == 0:
        print (zz)
    elif index % 5 == 0:
        zz = "Buzz"
        print (zz)
    print (index)
    index += 1