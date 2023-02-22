# The exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

def main():
    num = int(input("Please enter a number: "))
    odd_even = num % 2
    if odd_even == 0:
        print("Your number is divisible by 2!! Evens baby!")
    else:
        print("Your number was not divisible by 2 must be odd")

    check = int(input("Please enter a number to divide by: "))
    wholenum = num % check 
    if wholenum == 0:
        print(f"Damn, this number divides evenly from your two inputs. The outcome is {num/check}")

    else:
        print(f'This number is not evenly divisible, the outcome is {num/check}')



if __name__ == "__main__":
    main()