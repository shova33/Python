number = int(input("Enter the number: "))
digits = [int(d) for d in str(number)]
power = len(digits)
sum_digits = sum(d ** power for d in digits)
if sum_digits == number:
    print("Narcissistic Number")
else:
    print("Not a Narcissistic Number")
