import sys
import math

def isPrime(x):
    for m in range(2,int((math.sqrt(x)+1))):
        if x%m==0:
            return False
    return True

targetNumber = 600851475143

listOfFactors = list()

for x in range(1,int((math.sqrt(targetNumber)+1))):
    m = targetNumber%x
    if m==0:
        listOfFactors.append(x)

listOfFactors.reverse()

for x in range(len(listOfFactors)):
    if isPrime(listOfFactors[x]):
        print "The answer is " + str(listOfFactors[x])
        sys.exit()

print "No solution found."
