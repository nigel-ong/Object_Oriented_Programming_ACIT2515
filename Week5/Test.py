import random

def add (a,b):
    value = a *2
    return value + b


for iteration in range(10):
    number1 = random.randint(0,100)
    number2 = random.randint(0,100)
    result = add(number1,number2)
    pass