def sum_generator():
    sum=0
    while True:
        n=int(input("Enter a number: "))
        sum+=n
        if sum>100:
            print("Sum has exceeded 100")
            break
        yield sum

add_number=sum_generator()
for sum in add_number:
    print(sum)
    