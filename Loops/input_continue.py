# print("Enter 5 numbers (comma-separated):") #3,4,5,0,8
# n=list(map(int,input().split(','))) #map(func,iterator)
# sum=0
# for i in n:
#     if i==0:
#         continue
#     sum+=i
# print(f"Sum of numbers = {sum}")

print("Enter names of 5 people (space separated): ")
names_list = input().split(' ')
name = input("Enter name to search: ")
for i in names_list:
    if i == name:
        print(f"{name} found")
        break
else:
    print(f"{name} not found")