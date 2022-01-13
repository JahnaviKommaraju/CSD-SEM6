def reverse_factorial(num):
    n = 1
    i = 1
    while n < num:
        i += 1   
        n *= i
    return i

print(reverse_factorial(int(input())))

# 120
# n=1
# i=1

# 1<120
#  i=2 3 4 5  
#  n=2 6 24 120
