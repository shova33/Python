number = int(input("Enter a number: "))
while number >= 10:
    number = sum(int(digit) for digit in str(number))
print("Single digit sum:", number)
