n=int(input("Enter a number: "))
sum=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        sum+=i
        if i!=n//i:
            sum=sum+n//i
print(sum)