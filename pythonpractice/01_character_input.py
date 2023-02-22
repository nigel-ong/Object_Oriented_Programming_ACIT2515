# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

today = datetime.date.today()
year = today.year

def main():
    print(year)
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    linesprinted = int(input('How many times do you want this printed: '))
    hunna = year + (100-age)

    for i in range(linesprinted):
        print(f'Hi, {name}, you are {age} years old. In {hunna} you will be 100 years old\n')



if __name__ == "__main__":
    main()