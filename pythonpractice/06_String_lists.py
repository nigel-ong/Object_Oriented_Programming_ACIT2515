# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

word = input("Please enter a single word, no spaces: ").upper().strip()
if word == word[::-1]:
    print(word,"is a palindrome")

else:
    print(word," is not a palindrome")


# single line if-else
# print(word,"is a palindrome") if word == word[::-1] else print(word," is not a palindrome")