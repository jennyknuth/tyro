#This program asks the user to guess a random
# number between 0 and 100

import random
randomanswer = random.randint(0, 100)
#print ("answer", randomanswer)

answer = randomanswer
tries = 0
print ("I am thinking of a number between 0 and 100")

while tries < 20: # While statements check a Boolean variable
	guess = int(input("What's the number? "))
	if guess < answer:
		print("That's too low")
		tries += 1
		#print (tries)
	elif guess > answer:
		print ("That's too high")
		tries += 1
		#print (tries)
	else:
		print("Correct!")
		tries += 1
		if tries == 1:
			print("Lucky guess! You got it on your first try!")
		else:
			print("It took you %d guesses." % tries)
		break #if you write a program with a "while True" you need a "break"
if tries == 20:
		print("Bad luck! I don't think you're trying, start again!")
		
		
 
		
		
