import random
import time
from os import system

while True:
    e = 0
    try:
        system('cls')
        pool = input("Please enter multiple numbers to be sorted using commas (,) inbetween (ex. 1,2,3,4):\n").split(",")

        if len(pool) <= 1:
            raise Exception("no")
        elif all(pool[i] == pool[i+1] for i in range(len(pool)-1)):
            raise Exception("no")

        for i in pool:
            pool[e] = int(pool[e])
            e += 1
            
        hold = 0
        n = 1

        def shuf(a):
            random.shuffle(a)

        def sort(a):
            i = 0
            while i <= len(a)-2:
                    if a[i] > a[i+1]:
                        hold = a[i+1]
                        a[i+1] = a[i]
                        a[i] = hold
                        print(a, "\n")
                    i += 1
                    if all(pool[i] <= pool[i + 1] for i in range(len(pool)-1)):
                        print("DONE!")
                        break

        shuf(pool)
        while not all(pool[i] <= pool[i + 1] for i in range(len(pool)-1)):
            print("Step {}: ".format(n))
            sort(pool)
            input("Press enter to continue.\n")
            n += 1

    except:
        system('cls')
        print("Invalid input. Please try again.")
        time.sleep(2)
        system('cls')
        
    

  
     

