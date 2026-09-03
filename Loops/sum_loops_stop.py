sum=0
while True:
    n=int(input("Enter a number: "))
    sum+=n
    if sum<100:
        print(f"Sum is {sum}")
    else:
        print("Sum has exeeced 100")
        break