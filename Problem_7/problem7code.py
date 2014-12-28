import math

def isPrime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if x%i==0:
            return False
    return True

primes = list()
number = 2
while( len(primes)!=10001 ):
    if isPrime(number):
        primes.append(number)
    number = number + 1
print "ANSWER: " + str(primes[10001-1])
