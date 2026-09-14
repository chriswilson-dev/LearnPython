n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     if i<=(n+1)/2:
#         stars = i
#     else:
#         stars = (n+1)%i
#     for j in range(stars):
#         print("*", end="")
#     print()

middle = n // 2
for i in range(n):
    spaces = abs(middle - i)
    stars = n - (2 * spaces)
    for j in range(spaces):
        print(" ", end="")
    for j in range(stars):
        print("*", end="")
    print()