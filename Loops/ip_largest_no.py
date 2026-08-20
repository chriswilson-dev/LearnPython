largest_no=0
while True:
    n=int(input("Enter a number: "))
    if n>largest_no:
        largest_no=n
    if n==0:
        break
print(largest_no)