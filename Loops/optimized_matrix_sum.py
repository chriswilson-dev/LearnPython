matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sum=[0]*len(matrix)
col_sum=[0]*len(matrix[0])

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        row_sum[i]+=matrix[i][j]
        col_sum[j]+=matrix[i][j]
print(row_sum)
print(col_sum)