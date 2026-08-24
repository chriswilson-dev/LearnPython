# print(2)
# for i in range(3, 101, 2):
#     isPrime = True
#     for j in range(3, i, 2):
#         if i % j == 0:
#             isPrime = False
#             break
#     if isPrime == True:
#         print(i)

print(2)
for i in range(3, 101, 2):
    isPrime = True
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            isPrime = False
            break
    if isPrime == True:
        print(i)