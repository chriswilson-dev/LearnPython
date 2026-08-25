n=int(input("Enter a number: "))
cubes=list(map(lambda x:x**3,range (1,n+1)))
print(cubes)

# n = int(input("Enter n: "))
# Generator: more memory-efficient, computes on-the-fly
# cubes_generator = (i**3 for i in range(1, n + 1))
# Consume and print the generator
# for cube in cubes_generator:
#     print(cube)

# cubes=[i**3 for i in range(1,n+1)]
