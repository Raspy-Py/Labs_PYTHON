c = float(input("Enter hypotenuse: "))
a = float(input("Enter first leg: "))

if c <= a or (c <= 0 or a <= 0):
    print("This triangle doesn't exist!")
else:
    b = ((c) ** 2 - (a) ** 2) ** 0.5
    r = (a + b - c) / 2
    print("The radius of the inscribed circle:", r)