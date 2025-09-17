limit = int(input("Enter a number"))
fibo_series = []
a , b = 0 ,1
while ( a <= limit) :
    fibo_series.append(a)
a , b = b, a+b
print("The fibonacci series is :" , fibo_series)
