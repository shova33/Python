#TO find even odd number take a number input from user and then using conditionals divide the number by two if the modulusSim is zero then its even otherwise its odd.
user_input = int(input("Enter a Number: "))
print("You have entered the number:", user_input)
if user_input % 2 == 0:
    print("The entered number is even")
else:
    print("The entered number is odd")
