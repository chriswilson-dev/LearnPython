n=int(input("Enter a number n: "))
# num=1
# for i in range (1,n+1):
#     for j in range(1,i+1): #this was for the no. of numbers to be printed
#         print(num,end=" ")
#         num+=1
#     print()
num=1
for i in range (1,n+1):
    for j in range(1,i+1):
        if num>9:
            print(0,end=" ")
            num=1
        else:
            print(num,end=" ")
            num+=1
    print()