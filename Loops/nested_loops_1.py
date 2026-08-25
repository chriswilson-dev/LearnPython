# for i in range (1,6):
#     for j in range(1,11):
#         table=i*j
#         print(f"{i}x{j}={table}")
#     print()

tables=[[i*j for j in range (1,11)] for i in range (1,11)]
print(tables)