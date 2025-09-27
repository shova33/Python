def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
sum_primes = 0
for num in range(start, end + 1):
    if is_prime(num):
        sum_primes += num
print("Sum of prime numbers:", sum_primes)
