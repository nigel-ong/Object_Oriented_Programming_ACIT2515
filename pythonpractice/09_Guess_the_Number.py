import random
rn= random.randint(1,10)
counter = 0
print(rn)

guess = 0


while guess != rn :
    guess = input("Guess the number between 1-10: ") 
    while guess not in ["1","2","3","4","5","6","7","8","9","10"]:
        print("invalid")

    if int(guess) < rn:
        print("Too low")
        counter += 1
    elif int(guess) > rn:
        print("Too high")
        counter += 1
    else:
        counter += 1
        print(f"You found da number, you took {counter} guesses")
        
