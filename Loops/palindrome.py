n=int(input("Enter a number: "))
number=n
reverse=0
while n>0:
    reverse=(reverse*10)+(n%10)
    n=n//10
if reverse==number:
    print("n is a palindrom")
else:
    print("n is not a palindrome")
