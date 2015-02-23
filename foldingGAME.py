# Assignment 3, Problem 4, CSCI 1310
# Author: Jenny Knuth
# Date: 1/28/2015

# This program, about folding paper in half,
# explores different ways to calculate powers of 2

import math #plan to use pow function

thickness = .005 #cm

# Prompt user for input
print (("Your paper is %scm thick.") % thickness)
folds = input ("How many times would you like to fold your paper in half? ")

# Calculate thickness using powers of 2, since the thickness doubles each fold
totalthickness = thickness * math.pow(2, float(folds))
#print ("total thickness", totalthickness) #to test

# Calculate thickness using bitwise shift left, another way to double the value after each fold
#print ("binary folds", (1<<int(folds)))
binarythickness = .005 * (1<<int(float(folds)))
#print ("bitwise thickness", binarythickness)

# Output to user
#could substitue binarythickness for totalthickness
print()
print (("The thickness after %s folds will be %.2fcm.") % (folds, totalthickness)) 

# another way to calculate doubling would be to iterate 
# through a loop and increment thickness by thickness each time
# any other ways?
print ()
print ("Using a for-loop to double values:")
#loop for powers of 2
for i in range(1, (int(float(folds)+1))): #add 1 so it is inclusive of folds
	#print ("thickness", thickness * (2**i)) #does not use pow function
	thickness = thickness+thickness
	print (thickness, "cm")
print (("The thickness after %s folds will be %.2fcm.") % (folds, thickness)) 
