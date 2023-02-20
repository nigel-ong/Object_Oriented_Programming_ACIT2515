# ## ---------- In-class code.

# class Card:
#     def __init__(self,value,color):
#         try:
#             value = int(value)
#         except ValueError as e:
#             raise AttributeError(e)

#         if value < 1 or value > 10:
#             raise AttributeError

#         # wrong
#         # if not 0 < value < 10:
#         #     raise AttributeError

#         if color.lower() not in ("red", "black"):
#             raise AttributeError
        
#         self.value = value
#         self.color = color

#     def is_stronger_than(self,other):
#         return self.value > other.value


###----------------------------- my test code


class Card:
    def __init__ (self, value, color):
        if type(value) == str:
            if value.isnumeric() is True:
                value = int(value)
            else:
                pass
        else:
            pass
        valid_color = ['red','black']
        if not value or type(value) is not int or value not in range(1,11):
            raise AttributeError("Must be a number between 1 to 10! Please try again")
        if color.lower() not in valid_color:
            raise AttributeError("The color of the card must be 'Red' or 'Black'! Please try again")
        self.value = value
        self.color = color
    def is_stronger_than(self,Card):
        if self.value > Card.value:
            return True
        return False




# -----------------------------------------

    # def is_less_than(self,card):
    #     return not self.is_stronger_than(card)

# Card1 = Card(10,"Red")
# Card2 = Card(1,"Black")


# print(Card1.is_stronger_than(Card2))
# print(Card2.color)
# print(Card2.is_stronger_than(Card1))

# class Fruit:
#     def __init__(self,color):
#         self.color = color

# apple = Fruit('Red')


# class bank:
#     def __init__(self,amount =0):
#         self.balance =amount
# a = bank(124)
# b = bank()
# print(a.balance) #124
# print(b.balance) #0