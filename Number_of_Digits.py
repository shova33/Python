number = int(input("Enter the number: "))
count = 0
n = abs(number)
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1
print("Number of digits:", count)
