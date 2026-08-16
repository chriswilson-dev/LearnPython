n = int(input("Enter a number: "))
i = 1
sum = 0
while i < n:
    if n % i == 0:
        sum += i
    i += 1
if sum == n:
    print(n, "is a Perfect number")
else:
    print(n, "is not a Perfect number")