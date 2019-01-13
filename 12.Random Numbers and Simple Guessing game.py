# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 2019

@author: Byen23
"""

# This will be my 12th program to be uploaded to github

"""Random Numbers"""
'''The function random.randint returns a random number from among the numbers between the two arguments and including those numbers. The next session simulates the roll of a die 10 times:'''
import random
for roll in range(10):
	print(random.randint(1, 6), end = " ")
	
	

# Simple Guessing game using random, and a while True loop.
	
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = random.randint(smaller, larger)

count = 0
while True:
	count += 1
	userNumber = int(input("Enter your guess: "))
	if userNumber < myNumber:
		print("Too Small!")
	elif userNumber > myNumber:
		print("Too Large!")
	else:
		print("Congratulation!, YOu've got it in", count, "tries!")
		break
	
		
		
