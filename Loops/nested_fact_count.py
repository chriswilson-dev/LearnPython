n = int(input("Enter n: "))

# Outer loop: for every number from 1 to n
for num in range(1, n + 1):
    # Inner loop: count factors up to sqrt(num)
    factor_count = 0
    sqrt_num = int(num ** 0.5)
    
    for i in range(1, sqrt_num + 1):
        if num % i == 0:
            factor_count += 1
            if i != num // i:
                factor_count += 1
    
    print(f"Number {num}: {factor_count} factors")