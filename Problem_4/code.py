"""
Problem Statement:
    Largest palindrome product

    A palindromic number reads the same both ways. The largest palindrome made 
    from the product of two 2-digit numbers is 9009=91*99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(x):
    rev = str(x)
    rev = rev[::-1]
    if str(x)==rev:
        return True
    return False

max = 0
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j):
            if (i*j)>max:
                max = i*j

print max
