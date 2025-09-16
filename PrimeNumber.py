#Prime number is a number which had no divisors other than 1 and itself.
user_input = int(input("Enter a number : "))
print("The entered number is:", user_input)
counter = 0
for i in range (1 , user_input + 1):
    if user_input % i == 0:
        counter += 1
        if counter == 2:
            print("The number is prime")
        else:
            print("The number is not prime")