# n=int(input("Enter no of terms:"))
# a=0
# b=1
# for i in range(0,n,+1):
#         print (a)
#         next=a+b
#         a=b
#         b=next


# ========== VERSION 1: Using temp variable (Easiest to understand) ==========
print("VERSION 1: Using temp variable")
n = int(input("How many Fibonacci numbers? "))

a = 0
b = 1

print(a)

for i in range(n - 1):
    print(b)
    temp = a + b
    a = b
    b = temp

print()

# ========== VERSION 2: Store in list (Better practice) ==========
print("VERSION 2: Store in list")
n = int(input("How many Fibonacci numbers? "))

fib = []
a = 0
b = 1

fib.append(a)

for i in range(n - 1):
    fib.append(b)
    temp = a + b
    a = b
    b = temp

print(fib)
print()

# ========== VERSION 3: Cleanest (Pythonic) ==========
print("VERSION 3: Cleanest version")
n = int(input("How many Fibonacci numbers? "))

fib = []
a, b = 0, 1

for i in range(n):
    fib.append(a)
    a, b = b, a + b

print(fib)