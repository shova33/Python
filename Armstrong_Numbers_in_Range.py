start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
armstrong_numbers = []
for num in range(start, end + 1):
    num_str = str(num)
    num_len = len(num_str)
    armstrong_sum = sum(int(digit) ** num_len for digit in num_str)
    if armstrong_sum == num:
        armstrong_numbers.append(num)
print("Armstrong numbers in range:", armstrong_numbers)
