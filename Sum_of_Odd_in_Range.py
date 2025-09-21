start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_odd = 0
for num in range(start, end + 1):
    if num % 2 != 0:
        sum_odd += num
print("Sum of odd numbers:", sum_odd)
