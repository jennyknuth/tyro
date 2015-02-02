#Loop through integers and print "Fizz" if it's divisible by 3
#Print "Buzz" if it's divisible by 5

counter = 0

zz = ""

while counter < 20:
	if counter % 5 == 0 and counter % 3 == 0:
		print ("FizzBuzz ", end="")
		counter += 1
		#continue #can be dangerous to use since it won't go to increment the counter
		
	if counter % 3 == 0:
		print ("Fizz ", end="")
	elif counter % 5 == 0:
		print ("Buzz ", end="")
	counter += 1
	#print("counter", counter)
	
	if counter >20:
		break
		
#try it with string concatenation zz="" zz+="Fizz" zz+="Buzz" print(counter, zz)
print ()
print ()
#print ("new program")		
index = 0
#print ("index", index)

while index < 20:
	if index % 5 == 0 and index % 3 == 0:
		zz = "FizzBuzz"
		print (zz)
		index += 1
	elif index %3 == 0:
		zz = "Fizz"
		print (zz)
		index += 1
	elif index % 5 == 0:
		zz="Buzz"
		print (zz)
		index += 1
	else:
		#print ("new index", index)
		index += 1
		

		
