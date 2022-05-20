def add(a,b):
    answer= a+b
    return answer

def subtract(a,b):
    answer= a-b
    return answer

def multiply(a,b):
    answer=a*b
    return answer

def divide(a,b):
    answer=a/b
    return answer

def modulus(a,b):
    answer=a%b
    return answer

def intdivide(a,b):
    answer=a/b
    return answer

def exponent(a,b):
    answer= a**b
    return answer

def square(b):
    answer=b*b
    return answer

def cube(b):
    answer=b*b*b
    return answer

def factorial(b):
    fact =1
    for num in range(1, b+1):
        fact *=num
    return fact