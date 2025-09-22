number = int(input("Enter the number: "))
# Calculate factorial
fact = 1
for i in range(1, number + 1):
    fact *= i
# Sum the digits of the factorial
sum_digits = sum(int(d) for d in str(fact))
print("Sum of the digits of the factorial:", sum_digits)
