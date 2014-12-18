even_value_sum = 2
num1 = 1
num2 = 2

for x in range(3,4000000):
    num3 = num1 + num2
    if num3 > 4000000:
        break
    if num3 % 2 == 0:
        even_value_sum = even_value_sum + num3
    num1 = num2
    num2 = num3

print even_value_sum
