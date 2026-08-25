def lcm_is(a,b):
    larger=max(a,b)
    for i in range (larger,a*b+1,larger):
        if i%a==0 and i%b==0:
            return i
a,b=4,6
print("lcm is",lcm_is(a,b))
