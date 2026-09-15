n=int(input("Enter n: "))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for num in range(n,n-i,-1):
        print(num,end="")
    for num in range(n-i+2,n+1):
        print(num,end="")
    print()