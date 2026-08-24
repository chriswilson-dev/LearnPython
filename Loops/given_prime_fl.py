n = int(input("Enter a number: "))
isPrime = True
if n < 2:
    isPrime = False
elif n == 2:
    isPrime = True
elif n % 2 == 0:
    isPrime = False
else:
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            isPrime:False
            break
if isPrime:print("yes")
else: print("No")