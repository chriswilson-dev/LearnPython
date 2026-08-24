n = int(input("Enter a number: "))
factors = [i for i in range(1, int(n**0.5)+1) if n%i==0]
factors += [n//i for i in range(1, int(n**0.5)+1) if n%i==0 and i!=n//i]
print(sorted(factors))