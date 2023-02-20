def check_plate(plate):
        plate = plate.upper()
        num = [1,2,3,4,5,6,7,8,9]
        if plate[0] in num and plate[1] in num and plate[2] == "-" and plate[3].isalpha() and plate[4].isalpha() and plate[5] == "-" and plate[6] in num and plate[7] in num :
            return True
        else:
            return False
        

def find_next_plate(plate,num=1):
    
if __name__ == "__main__":
    print(check_plate("11-aa-11"))
        





