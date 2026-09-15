# for i in range(1, n + 1):
#     if i<=(n+1)/2:
#         stars = i
#     else:
#         stars = (n+1)%i
#     for j in range(stars):
#         print("*", end="")
#     print()

n = int(input("Enter n: "))

print(f"Diamond pattern of size {n}:\n")

# Calculate middle row
middle = (n + 1) / 2.0                # Line 1: Middle position

# Outer loop: n rows (YOUR LOGIC!)
for i in range(1, n + 1):             # Line 2: For each row
    
    # Calculate distance from middle
    distance = abs(i - middle)        # Line 3: How far from middle?
    
    # Calculate number of stars
    stars_count = 2 * int(middle - distance) - 1  # Line 4: Stars formula
    
    # Calculate number of spaces
    spaces_count = (n - stars_count) // 2  # Line 5: Center alignment
    
    # Print spaces
    for j in range(spaces_count):     # Line 6: Inner loop 1
        print(" ", end="")
    
    # Print stars
    for k in range(stars_count):      # Line 7: Inner loop 2
        print("*", end="")
    
    print()                            # Line 8: Newline

print()