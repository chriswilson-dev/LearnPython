n=int(input("Enter n: "))
print(2)
for i in range(3,n+1,+2):
    isPrime=True
    for j in range(2,int(i**0.5)):
        if i%j==0:
            isPrime=False
            break
    if isPrime:
        print(i)
