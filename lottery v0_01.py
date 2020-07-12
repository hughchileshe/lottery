'''This version of the of the program uses a list to iterate through the numbers'''

# Import statements
import random
import math

# Variable declaration
balls = int(input("Enter number of balls:\n"))
ballsDrawn = int(input("Enter number of balls to be drawn:\n"))

# Function definition for odds
# Uses the balls and ballsDrawn variables
def Odds(numOB, numBD):
    numX = math.factorial(numOB)
    numY = math.factorial(numBD)
    numZ = numX / (numY * (math.factorial(numOB - numBD)))
    return numZ

# Function definition for the random number generator.
# Uses the balls and ballsDrawn variables.
def randomNumberGenerator(numOB, numBD):
    listN = []
    while len(listN) < numBD:
        numX = random.randint(1, numOB)
        for index in range(len(listN)):
            if listN[index] == numX:
                numX = random.randint(1, numOB)
        listN.append(numX)
    return listN
