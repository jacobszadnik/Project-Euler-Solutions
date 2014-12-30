import sys
import math

for a in range(1,1001):
    for b in range(1+a,1001-a):
        for c in range(1+b,1001-a-b):
            if a**2+b**2==c**2:
                if a+b+c==1000:
                    print "ANSWER: " + str(a*b*c)
                    sys.exit()
