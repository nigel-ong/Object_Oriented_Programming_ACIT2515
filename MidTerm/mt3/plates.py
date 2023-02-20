def check_plate(plate):
    num="123456789"
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if plate[0] in num and plate[1] in num and plate[2] == "-" and plate[3] in abc and plate[4] in abc and plate[5] == "-" and plate[6] in num and plate[7] in num :
        return True
    else:
        return False

def find_next_plate(plate, increment:int=1):
    # plate[0] = int 
    # plate[1] = int 
    # plate[6] = int
    # plate[7] = int
    # plate[3] = alpha 65 = A
    # plate[4] = alpha 90 = Z
    plate = list(plate)
    plate[3] = ord(plate[3])
    plate[4] = ord(plate[4])

    plate[0] = int(plate[0])
    plate[1] = int(plate[1])
    plate[6] = int(plate[6])
    plate[7] = int(plate[7])
    plate[3] = int(plate[3])
    plate[4] = int(plate[4])

    #67 +57
    counter = increment
    plate_counter = 0 
    ord_counter = 0

    plate_counter = (counter+plate[7])%9
    counter = ((counter+plate[7])-plate_counter)//9
    plate[7] = plate_counter
    if plate[7] == 0:
        plate[7] = 9
        counter -= 1
            
    plate_counter = (counter+plate[6])%9
    counter = ((counter+plate[6])-plate_counter)//9
    plate[6] = plate_counter
    if plate[6] == 0:
        plate[6] = 9
        counter -= 1
    
    plate_counter = (counter+(plate[4]-64))%26
    counter = ((counter+(plate[4]-64))-plate_counter)//26
    ord_counter = plate_counter + 64
    plate[4] = ord_counter
    if plate[4] == 0:
        plate[4] = 1
     
    plate_counter = (counter+(plate[3]-64))%26
    counter = ((counter+(plate[3])-64)-plate_counter)//26
    ord_counter = plate_counter + 64
    plate[3] = ord_counter
    if plate[3] == 0:
        plate[3] = 1
    
    plate_counter = (counter+plate[1])%9
    counter = ((counter+plate[1])-plate_counter)//9
    plate[1] = plate_counter
    if plate[1] == 0:
        plate[1] = 9
        counter -= 1
    
    plate_counter = (counter+plate[0])%9
    counter = ((counter+plate[0])-plate_counter)//9
    plate[0] = plate_counter
    if plate[0] == 0:
        plate[0] = 9
    if counter >= 1:
        raise OverflowError("Impossible to find next plate")

    
    plate[3] = chr(plate[3])
    plate[4] = chr(plate[4])
    plate[0] = str(plate[0])
    plate[1] = str(plate[1])
    plate[6] = str(plate[6])
    plate[7] = str(plate[7])

    join_plate = "".join(plate)
    return(join_plate)

def main():
    print(find_next_plate("11-AA-11", 1000000))
    # print(find_next_plate("11-AA-11", 8))
    # print(find_next_plate("11-AA-11", 81))
    # print(find_next_plate("11-BZ-11", 81))
    # print(find_next_plate("15-ZZ-12", 80))
    # print(find_next_plate("99-ZZ-99"))
    # print(find_next_plate("99-ZZ-98", 2))

if __name__ == "__main__":
    main()