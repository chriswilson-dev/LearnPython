n=int(input("Enter no of rows: "))
for row in range(1,n+1):
    print (f"Row {row}:",end=" ")
    a,b=0,1
    for j in range(row): #which is also range(0,row,1)
        print(f"{a} ",end="")
        a,b=b,a+b
    print()