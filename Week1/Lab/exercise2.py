textfile = 'data01.txt'
# textfile = 'people_3.txt'

def count_people(file):
    with open(file, 'r') as txt:
        content = txt.read()
        return (content.split())
    
def count_unique_people(file):
    unique_names = (count_people(file))
    return set(unique_names)


def main():

    print("Number of lines in file:", len(count_people(textfile)))
    print("Number of unique lines in file:", len(count_unique_people(textfile)))

if __name__ == "__main__":
    main()



##----------------------------------

## in class code


# def count_people(file):
#     with open(file, "r") as text:
#         return len(text.readlines())
    

# def count_unique_people(file):
#     with open(file) as my_file:
#         unique_set = set([line.strip() for line in my_file.readlines()])
#         return len(unique_set)



# def main():
#     print(count_unique_people('tim.txt'))

# if __name__ == "__main__":
#     main()