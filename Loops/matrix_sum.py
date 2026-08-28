matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rows=len(matrix)
cols=len(matrix[0])
#rows sum

for i in range(rows):
    row_sum=0
    for j in range(cols):
        row_sum+=matrix[i][j]
    print(f"Row {i+1} sum = {row_sum}")

#cols sum
for i in range(cols):
    col_sum=0
    for j in range (rows):
        col_sum+=matrix[j][i]
    print(f"Col {i+1} sum = {col_sum}")

