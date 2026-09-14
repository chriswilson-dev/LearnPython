# import string
n=int(input("Enter no. of rows: "))
# letters=string.ascii_uppercase
# index=0
# for i in range(1,n+1):
#     for j in range(i): #same as (1,i+1) but we don't use j
#         print(letters[index], end=" ") #we have to run this exactly i times
#         index+=1
#     print()
    # letter='A'
    # for i in range (1,n+1):
    #     for j in range(1,i+1):
    #         print(letter, end=" ")
    #         letter=chr(ord(letter)+1)
    #     print()
letter='A'
for i in range(1,n+1):
    for j in range(1,i+1):
        print(letter,end=" ")
    print()
    letter=chr(ord(letter)+1)