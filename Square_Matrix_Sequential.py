size = int(input("Enter the size of the matrix: "))
num = 1
for i in range(size):
    row = []
    for j in range(size):
        row.append(str(num))
        num += 1
    print(' '.join(row))
