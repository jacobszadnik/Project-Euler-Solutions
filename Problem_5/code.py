def evenlyDivisibleOneThroughTwenty(x):
    for i in range(1,21):
        if x%i!=0:
            return False
    return True

number = 20	
while(True):
    if evenlyDivisibleOneThroughTwenty(number):
        print "ANSWER: " + str(number)
        break
    else:
        number = number + 20
