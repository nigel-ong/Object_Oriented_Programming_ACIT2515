def check_plate(plate):
    num="123456789"
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plate_split = list(plate)
    if plate[0] in num and plate[1] in num and plate[2] == "-" and str(plate[3]).isalpha() and str(plate[4]).isalpha() and plate[5] == "-" and plate[6] in num and plate[7] in num :
        return True
    else:
        return False

def find_next_plate():
    pass

def main():
    print(check_plate("11-ff-11"))

if __name__ == "__main__":
    main()