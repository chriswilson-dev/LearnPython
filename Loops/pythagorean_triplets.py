n = int(input("Enter n: "))

# Outer loop: for each possible 'a'
for a in range(1, n + 1):              # Line 1: First number a
    # Middle loop: for each possible 'b' (b >= a)
    for b in range(a, n + 1):          # Line 2: Second number b
        # Inner loop: for each possible 'c' (c > b)
        for c in range(b + 1, n + 1):  # Line 3: Third number c
            # Check if it's a Pythagorean triplet
            if a*a + b*b == c*c:       # Line 4: Check Pythagorean condition
                print(f"({a}, {b}, {c})")  # Line 5: Print if valid