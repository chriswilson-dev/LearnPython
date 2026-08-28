matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row_sum=[sum(i)for i in matrix]
col_sum=[sum(j)for j in zip(*matrix)]
print(row_sum)
print(col_sum)