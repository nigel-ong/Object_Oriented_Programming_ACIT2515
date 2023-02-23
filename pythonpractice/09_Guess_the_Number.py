import random
x= random.randint(1,10)
count =[]
print(x)

a = 0
running = True

while running:

    a = int(input("guess1"))

    if a == 55:
        running = False
    if a < x:
        print("too low")
    elif a > x:
        print("too high")
    else:
        print("you found da number")
input()
