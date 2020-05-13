'''This is a lottery random number generating application written in Python.'''

#import statements
import math
import random

#variable declaration
ballsDrawn = 6
numberOfBalls = int(input('Number of balls:\n>'))
entries = int(input('Number of entries:\n>'))

#Random number generator function
def randomNumberGenerator(numberOfBalls):
	one = random.randint(1, numberOfBalls)
	two = random.randint(1, numberOfBalls)
	three = random.randint(1, numberOfBalls)
	four = random.randint(1, numberOfBalls)
	five = random.randint(1, numberOfBalls)
	six = random.randint(1, numberOfBalls)

	while two == one:
		print('two:',two)
		two = random.randint(1, numberOfBalls)

	while three == one or three == two:
		print('three:',three)
		three = random.randint(1, numberOfBalls)

	while four == one or four == two or four == three:
		print('four:',four)
		four = random.randint(1, numberOfBalls)

	while five == one or five == two or five == three or five == four:
		print('five:',five)
		five = random.randint(1, numberOfBalls)

	while six == one or six == two or six == three or six == four or six == five:
		print('six:',six)
		six = random.randint(1, numberOfBalls)

	return one, two, three, four, five, six

# function: numberOfEntries
# Takes variables: entriesand numberOfBalls, and function: randomNumberGenerator
# 
def Entries(e,nob, f):
	for i in range(e):
		print(f(nob))
		
# Function: Odds
# Calculates based on the number of balls and entries
def Odds(numberOfBalls, ballsDrawn):
	nobFactorial = math.factorial(numberOfBalls)
	bdFactorial = math.factorial(ballsDrawn)
	odds = nobFactorial / (bdFactorial*(math.factorial(numberOfBalls-ballsDrawn)))
	print(odds)
	

	
Odds(numberOfBalls, ballsDrawn)
#print(Entries(entries, numberOfBalls, randomNumberGenerator))
