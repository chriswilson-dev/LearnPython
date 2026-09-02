# for i in range(1,101):
#     if i%5==0:
#         continue
#     print(i)

def numbers_not_div_by_5(limit):
    for num in range(1, limit + 1):
        if num % 5 != 0:
            yield num

for n in numbers_not_div_by_5(100):
    print(n)
