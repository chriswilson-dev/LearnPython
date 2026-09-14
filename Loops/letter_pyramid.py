n=int(input("Enter a number: "))
# letter='A'
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("",end=" ")
#     for k in range((i*2)-1):
#         print(letter,end="")
#         letter=chr(ord(letter)+1)
#     print()
for i in range(1,n+1):
    for j in range(n-i):
        print("",end=" ")
    for k in range(1,i+1):
        print(k,end="")
    for k in range(i-1,0,-1):
        print(k,end="")
    print()
