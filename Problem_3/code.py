
"""
Problem Statement:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

####################
##  The largest prime factor of a number
## will be equal to or less than the
## square root of that number.
####################

"""
First we will find all the prime
numbers less than the square root of
our target number
"""
targetNumber = 600851475145
sqRtOfTargetNumber = targetNumber**(1/2)
primeNumbers []
for x in range(2,int(sqRtOfTargetNumber)):
    primeNumbers.append(x)
currentPrime = 0
