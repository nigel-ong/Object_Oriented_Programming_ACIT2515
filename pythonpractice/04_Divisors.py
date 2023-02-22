def main():
    divisor_list = []
    num = int(input("Please enter a number: "))
    for i in range(1,(num+1)):
        if num % i == 0:
            divisor_list.append(i)
    print("what up", divisor_list)

    #list comp
    print(f"sup {[i for i in range(1,num+1) if num%i ==0]} dis nibba")


if __name__ == "__main__":
    main()