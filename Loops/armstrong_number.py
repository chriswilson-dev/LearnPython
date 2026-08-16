n = int(input("Enter a number: "))
power = len(str(n))
original = n
sum = 0
while n > 0:
    sum = sum + (n%10) ** power
    n //= 10
if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")