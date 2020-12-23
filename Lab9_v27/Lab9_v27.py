def numerizor(a):
    res = []
    print("Numbers: ", end='')
    for i in a:
        n = ord(i)
        if n>=48 and n<=57:
            res.append(n-48)
            print(n-48, end=' ')
    return res

def sumator(b):
    sum = 0
    for i in b:
        sum += i
    return sum;

string = input("Type something: ")
numbers = numerizor(string)
sum = sumator(numbers)
print("\nSum: ", sum)