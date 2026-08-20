n=int(input("Enter the number: "))
i=1
factors=[]
while i*i<=n:
    if n%i==0:
        factors.append(i)
        if i!=n//i:
            factors.append(n//i)
    i+=1
factors.sort()
print(f"Factors of {n} are {factors}") #f means a formatted string
#f looks for {} and replaces the variables in it with a value