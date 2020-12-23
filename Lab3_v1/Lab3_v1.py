Sum = 1
Nc = 1
Np = 0
Eps = 0.0001
N = 1

X = float(input("Enter X: "))

if X >= 0 and X <= 4:
    while abs(Nc + Np) > Eps:
        Np = Nc
        Nc = Nc * (-1) * X * X / ((2 * N - 1) * (2 * N))
        Sum += Nc
        N += 1
    print("Sum: ", Sum)
else:
    print("Invalid value of X=", X, sep='')