def factorial(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
def calculateE(accuracy):
    e = 1.0
    n = 1.0
    differ = 0.0
    previous = 0.0
    while differ < accuracy and n < 17: # n < 17 because that is how far decimals went on cygwin, onwards the numbers would be the same and the difference would be 0
        previous = e
        e += float(1/factorial(n))
        differ = float(e - previous)
        n += 1
    return float(e)

x= float(input("Write an approximate accuracy value: "))
print (("The approximate value of e is: ")+ str(calculateE(x)))
