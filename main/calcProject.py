#Joey Jiemjitpolchai
import math
def calcSin(x):
    output = 0
    for k in range(0, term+1):
        output += ((-1)**k) * (x**(2*k+1))/math.factorial(2*k + 1)
    return output
def calcCos(x, term):
    output = 0
    for k in range(0, term+1):
        output += (((-1)**k) * (x**(2*k)))/math.factorial(2*k)
    return output

print("Scientific Calcuator")
x = input('Enter your function:')
print("Test", calcCos(int(x), 2))
