start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_even = 0
for num in range(start, end + 1):
    if num % 2 == 0:
        sum_even += num
print("Sum of even numbers:", sum_even)
