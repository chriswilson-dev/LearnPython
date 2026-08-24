n=int(input("Enter no of terms:"))
sum=0
a=0
b=1
for i in range(0,n):
    sum+=a
    a=b
    b=a+b  # ✓ CHANGE THIS LINE!
print(sum)