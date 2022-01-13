from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

d = b**2 - 4*a*c

if d > 0:
    num_roots = 2
    x1 = (((-b) + sqrt(d))/(2*a))     
    x2 = (((-b) - sqrt(d))/(2*a))
    print('the roots are',int(x1),int(x2))

elif d == 0:
    num_roots = 1
    x = (-b) / 2*a
    print('the root is',int(x))    

else:
    print("No real roots")