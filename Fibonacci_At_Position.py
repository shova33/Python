position = int(input("Enter the position: "))
if position <= 0:
    print("Position must be a positive integer.")
else:
    a, b = 0, 1
    for i in range(1, position):
        a, b = b, a + b
    print(f"Fibonacci number at position {position} is {a}")
