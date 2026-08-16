n=int(input("Enter a number: "))
flag=True
i=2
while i<n:
    if n%i==0:
        flag=False
        break
    else: i=i+1
if flag:
    print("This number {} is a prime_number".format(n))
else:
    print("This number {} is not a prime".format(n))
