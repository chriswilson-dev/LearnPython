# print("Enter 5 numbers (comma-separated):") #3,4,5,0,8
# n=list(map(int,input().split(','))) #map(func,iterator)
# sum=0
# for i in n:
#     if i==0:
#         continue
#     sum+=i
# print(f"Sum of numbers = {sum}")

print("Enter names of 5 people (comma separated): ") #list we have
n=list(input().split(','))
print("Enter name to be searched: ")
name=input() #whom we are searching for
for i in n:
    if name==i:
        print("name found")
        break
else:
    print("name not found")