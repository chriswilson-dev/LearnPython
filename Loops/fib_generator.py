n=int(input("Enter no of rows: "))
def fib_generator():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib_next=fib_generator()
for i in range (1,n+1):
    print(f"Row {i}:",end=" ")
    for j in range(i):
        print(next(fib_next),end=" ")
    print()
    