n = int(input("Enter a number: "))
isPrime = [True] * (n + 1)  # we created a list from 0
isPrime[0] = isPrime[1] = False  # 0 and 1 are already not prime
for i in range(2, int(n ** 0.5) + 1):  # starting from 2 till the sqrt
                                       # root plus 1
    if isPrime[i]:  # if still prime then enter the inner loop
                    # and mark all the multiples as not prime
        for j in range(i * i, n + 1, i):
            isPrime[j] = False
for k in range(2, n + 1):  # checking from 2 cuz we already know
                           # that 0 and 1 are not prime
    if isPrime[k] == True:
        print(k)