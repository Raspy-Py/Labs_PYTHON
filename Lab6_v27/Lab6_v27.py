from math import pi

def min_value(a, b):
    return b if a <= b else a

a = int(input("Enter a: "))
b = int(input("Enter b: "))

U = min_value(a, b)
V = min_value(a * b, a + b)
W = min_value(U + V ** 2, pi)

print("U = ", U, "\nV = ", V, "\nW = ", W, sep='')