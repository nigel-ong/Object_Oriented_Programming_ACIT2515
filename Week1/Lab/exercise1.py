def str2dict(text):
    my_dict = {}
    for char in text:
        if char not in my_dict:
            my_dict[char] = 1 
        else:
            my_dict[char] += 1
    return my_dict

def str2dict_Plus(text2:str):
    rmvp = ''
    for letter in text2:
        if letter.isalpha() == True:
            rmvp += letter 
    return str2dict(rmvp.lower())
    
def histogram(string:str):
    string_input = str2dict_Plus(string)
    for letter in string_input.items():
        print(letter[0], letter[1]*'*')


def main():
    text = input("Enter in a phrase, will return each character and its frequency: ") 
    string1 = str2dict(text)
    string_plus = str2dict_Plus(text)
    string_star = histogram(text)
    # print(string1)
    # print(string_plus)
    string_star
    
if __name__ == "__main__":
    main()

##----------------------------------

## in class code

# def str2dict(word:str) -> dict[str, int]:
#     new_dict = {}
#     for letter in word:
#         letter_occurr = word.count(letter)
#         # new_dict.update({letter: letter_occurr})
#         new_dict[letter] = letter_occurr
#     return new_dict
    

# def str2dict_plus(word:str) -> dict[str, int]:
#     clean_word = ""
#     for letter in word.strip().lower():
#         if letter.isalpha():
#             clean_word += letter
#     return str2dict(clean_word)


# def histogram(word:str):
#     for key, value in str2dict_plus(word).items():
#         print(f'{key} {"*" * value}')

# def main():
#     print(str2dict("Hello!"))
#     print(str2dict_plus("Hello World!")) 
#     histogram("Hello World!")

# if __name__ == "__main__":
#     main()