def triangle(size):
    """ This function must print a triangle using the # character on the screen.

    Example:
    >>> triangle(5)
    #
    ##
    ###
    ####
    #####

    """

    for i in range(size):
        if i >= 0:
            print((i+1)*'#')
        else:
            print(i)


def rectangle(width, height):
    """ This function must print a rectangle with the correct dimensions on the screen with #.

    !!! The rectangle is not filled with # !!!

    Examples:
    >>> rectangle(0, 0)
    
    >>> rectangle(1, 1)
    #
    
    >>> rectangle(3, 1)
    ###
    
    >>> rectangle(10, 3)
    ##########
    #        #
    ##########

    """



    for h in range(height):
        print('#'*width)   


    ##----------------------------------

    ## in class code

    # if height >= 1:
    #     print("#" * width)
    
    # for line in range(1, height - 1):
    #     print("#" + (width - 2) * " " + "#")
        
    # if height >= 2:
    #     print("#" * width) 
    ##----------------------------------

    
    # w = 0
    # h = 1
    # while w < width:
    #     print('#',end="")
    #     w += 1
    
        # if w == width:
        #     print('\nj')
        #     print('#\n')
            # while h <= height:
            #     h += 1
            
        



    
    # h = 0
    # if width or height > -1:
    #     if range(height[:len(height)]) == [0] or [-1]:
    #         for w in range(width):
    #             print('#',end="")
    #             if w == (width-1):


            
            
                
        

    # if width or height > -1:
    #     for h in height:
    #         if height[h] == 0 or -1:
    #             for w in range(width):
    #                 print('#',end="")

    # if width or height > -1:
    #     for i in range(width):
    #         print()
    #         for i in range(height):
    #             print('#',end="")

    


    # for w, h in width, height:
    #     if w <= 0 and h <= 0:
    #         print('Enter positive width and height')
    #     else:
    #         print(w,h)

    #nested for loop?

    

if __name__ == "__main__":
    # triangle(0)
    # triangle(10)

    rectangle(6, 4)
    # rectangle(-1, -1)



##----------------------------------

## in class code