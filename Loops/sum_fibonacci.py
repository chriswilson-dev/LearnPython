n=int(input("Enter n upto which you want the sum: "))
a=0
b=1
i=1
sum=0
if n==1: print("0") 
else :
    while i<=n: 
        sum=a+b 
        a=b 
        b=sum
        i+=1
    print (sum)