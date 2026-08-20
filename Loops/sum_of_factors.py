n=int(input("Enter a number: "))
i=1
factors=[]
while i*i<=n:
    if n%i==0:
        factors.append(i)
        if i!=n//i:
            factors.append(n//i)
    i+=1
print(f"Sum of factors = {sum(factors)}")