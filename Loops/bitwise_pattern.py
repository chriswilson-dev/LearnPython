n=int(input("Enter no. of rows: "))
value=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(value, end=" ")
        value^=1
    print()
