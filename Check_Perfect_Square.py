import math
number = int(input("Enter a number: "))
sqrt = int(math.sqrt(number))
if sqrt * sqrt == number:
    print("True")
else:
    print("False")
