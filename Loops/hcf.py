a=int(input("Number 1: "))
b=int(input("Number 2: "))
while b!=0:
    a,b=b,a%b
print(f"HCF: {a}")