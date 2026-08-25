def hcf_brute(a, b):                    # no 'self' needed, it's not a class method
    smaller = min(a, b)                  # hcf cannot be greater than the smaller no.
    hcf = 1
    for i in range(1, smaller + 1):
        if a % i == 0 and b % i == 0:
            hcf = i
    return hcf                            # send the result back out

a, b = 36, 60
print(hcf_brute(a, b))                    # call the function with actual arguments