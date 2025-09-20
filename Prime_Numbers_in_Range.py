start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
primes = []
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)
print("Prime numbers in range:", primes)
