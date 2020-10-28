X = float(input("Enter X: "))
Y = float(input("Enter Y: "))

if Y > 1 - X:
    if X <= 0 or Y <= 0:
        print("The point belongs to the shaded area")
    else: 
        print("The point does not belong to the shaded area")
else:
    print("The point does not belong to the shaded area")