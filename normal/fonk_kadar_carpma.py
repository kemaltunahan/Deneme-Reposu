import time
def carp(sayi1,sayi2):
    a=0
    for i in range(sayi2):
        a+=sayi1
    return a
while(1):
    print("************ÇARPMA PROGRAMI**************")

    sayi1=int(input("İlk pozitif sayıyı giriniz:"))
    sayi2=int(input("İkinci pozitif sayıyı giriniz:"))

    if(sayi1>0 and sayi2>0):
        print("{} * {} = {}".format(sayi1,sayi2,carp(sayi1,sayi2)))

    else:
        print("Pozitif sayılar giriniz!!")

    sec=input("Devam etmek için herhangi bir tuşa basınız!!\nÇıkmak için k tusuna basınız:")
    if(sec=="k" or sec=="K"):
        print("Güle güle :))")
        time.sleep(2)
        break
