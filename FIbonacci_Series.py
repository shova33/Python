limit = int(input("Enter the limit: "))
fib_series = []
a, b = 0, 1
while a <= limit:
	fib_series.append(a)
	a, b = b, a + b
print(fib_series)
