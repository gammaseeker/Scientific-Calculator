#Joyce Feng
#Joey Jiemjitpolchai
import math
def calcCos(x, c, n):
    output = 0
    for k in range(0, n+1):
        output += (((-1)**k) * ((x-c)**(2*k)))/math.factorial(2*k)
    return output

def calcSin(x, c, n):
    sum = 0
    for i in range (0, math.ceil(n/2)):
        sum += ((-1)**i)*((x-c)**(2*i+1))/math.factorial(2*i+1)
    return sum

def calcLn(x, c, n):
    while(x < 0):
        x = int(input("Enter an x between the range of 1 to infinity."))
    while (c < 1):
        c = int(input("Enter a c between the range of 1 to infinity."))
    sum = math.log(c)
    for i in range (1, n+1):
            sum += (((-1)**(i+1))*((x-c)**i)/(i*(c**i)))
    return sum

def calcE(x, c, n):
    sum = 0
    for i in range (0, n+1):
        sum += ((x-c)**i)/math.factorial(i)
    return sum

def calcArcTan(x, c, n):
    sum = 0
    for i in range(0, math.ceil(n/2)):
        sum += ((-1)**i)*((x-c)**(2*i+1))/(2*i+1)
    return sum

def calcArcSin(x, c, n):
    while (x < -1 or x > 1):
        x = int(input("Enter a number between the range of -1 to 1."))
    sum = 0
    for i in range (0, math.ceil(n/2)):
        sum += ((-1)**i)*(math.factorial(2*i))*(x**(2*i+1))/((2**(2*i))*((math.factorial(i))**2)*(2*i+1))
    return sum

def calcArcCos(x, c, n):
    while (x < -1 or x > 1):
        x = int(input("Enter a number between the range of -1 to 1."))
    sum = (math.pi)/2
    for i in range (0, math.ceil(n/2)):
         sum -= ((math.factorial(2*i))*(x**(2*i+1)))/((2**(2*i))*((math.factorial(i))**2)*(2*i+1))
    return sum

print(calcSin(math.pi, 0, 5))
print(calcLn(3, 2, 3))
print(calcE(5, 0, 3))
print("Scientific Calcuator")
x = input('Enter your function:')
print("Test", calcCos(int(x), 2))
#print(calcSin(math.pi, 0, 5)
#print(calcLn(3, 2, 3))
#print(calcE(5, 0, 3))
#print("Scientific Calcuator")
#x = input('Enter your function:')
#print("Test", calcCos(int(x), 2))
print(calcLn(-1, 0, 100))

