while True:
    dec = int(input())
    if(dec<0):
            print("enter a valid number")
    else:
        print("the binary value of the given decimal is ", bin(dec)[2:])
        print("the octal value of the given decimal is ", oct(dec)[2:])
        print("the hexadecimal value of the given decimal is ", hex(dec)[2:])
        break
