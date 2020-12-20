def asal(a, b):  
    if (a.isdigit() == True):
        a = int(a)
        if (a > 3):
                for x in range(2, (a-1)):
                    if(a%x == 0):
                        b = 1
                        break
                    else:
                        b = 2
                if(b == 2):
                    print("asal")
                elif(b == 1):
                    print("asal deil")
        elif (a == 2 or a == 3):
            print("asal")
        elif (a == 1):
            print("asal deil")
    elif (a.isdigit() == False ):
        print("düzgün gir sayı olsun")
        asal(input("Sayı gir"), 0)
    if (input("başka sayı sorcaksan y gir") == "y"):
        asal(input("Sayı gir"), 0)
    else:
        print("ok bye")
        exit()

asal(input("Sayı gir"), 0)