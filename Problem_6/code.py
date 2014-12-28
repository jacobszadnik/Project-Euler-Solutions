sumOfSquares = 0
squareOfSum = 0
for i in range(1,101):
    squareOfSum = squareOfSum + i
    sumOfSquares = sumOfSquares + (i*i)

squareOfSum = squareOfSum*squareOfSum

ans = squareOfSum-sumOfSquares

print "ANSWER: " + str(ans)
