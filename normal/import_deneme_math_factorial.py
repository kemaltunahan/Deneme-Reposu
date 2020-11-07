import math
import time
while(True):
    sayi=int(input("Sayi gir:"))
    print("{}! = {}".format(sayi,math.factorial(sayi)))
    print("Devam etmek için herhangi bir tuşa basınız!!\nÇıkmak için c tuşuna basınız!!")
    press=input()
    if(press=="c" or press=="C"):
        print("GÜLE GÜLE :)))")
        time.sleep(2)
        break


    