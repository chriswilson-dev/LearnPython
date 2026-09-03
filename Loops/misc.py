# # Calculate and print the value of the series 
# # 1 + 1/2 + 1/3 + … + 1/n.
# n=int(input("Enter n: "))
# sum=0
# for i in range (1,n+1):
#     sum+=1/i
# print(sum)

# Calculate and print the value of the series
# 1! + 2! + 3! + … + n!.
n = int(input("Enter n: "))
fact = 1
sum = 0
for i in range(1, n + 1):
    fact=fact*i
    sum=sum+fact
print(sum)