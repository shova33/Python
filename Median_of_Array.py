array = input("Enter the array of numbers separated by spaces: ")
arr = list(map(int, array.split()))
arr.sort()
n = len(arr)
if n % 2 == 1:
    median = arr[n // 2]
else:
    median = (arr[n // 2 - 1] + arr[n // 2]) / 2
print("Median:", median)
