print("Start entering random numbers: ")
numbers=[] #numbers = list

while True:
    num=int(input())
    if  num < 0:
        print("Negative number encountered. Loop stopped")
        break
    else:
        numbers.append(num)
        print(f"{num} is not negative")