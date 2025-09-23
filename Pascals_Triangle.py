rows = int(input("Enter number of rows: "))
triangle = []
for i in range(rows):
    row = [1]
    if triangle:
        last_row = triangle[-1]
        for j in range(1, i):
            row.append(last_row[j-1] + last_row[j])
        row.append(1)
    triangle.append(row)
for row in triangle:
    print(' '.join(map(str, row)))
