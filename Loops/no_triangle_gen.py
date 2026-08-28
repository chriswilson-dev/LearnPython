n=int(input("Enter no of rows: "))
def number_generator():
    a=1
    while True:
        yield a
        a+=1
no_gen=number_generator()
for i in range(1,n+1):
    print(f"Row {i}:",end=" ")
    for j in range(i):
        print(next(no_gen),end=" ")
    print()
