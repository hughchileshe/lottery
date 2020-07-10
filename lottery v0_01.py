'''This version of the of the program uses a list to iterate through the numbers'''

# Import statements
import random
import math

# Variable declaration
ballsDrawn = 6
balls = 10

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
        listN.append(numX)
    return listN

