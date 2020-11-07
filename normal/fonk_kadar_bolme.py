import time
def bol(sayi1,sayi2):
    a=0
    while(sayi1>=sayi2):
        sayi1-=sayi2
        a+=1
    return a
while(True):
    print("******************BÖLME PROGRAMI*****************")

    sayi1=int(input("İlk pozitif sayıyı giriniz:"))
    sayi2=int(input("İkinci pozitif sayıyı giriniz:"))

    if(sayi1>0 and sayi2>0):
        print("{} / {} = {}".format(sayi1,sayi2,bol(sayi1,sayi2)))

    else:
        print("Pozitif sayılar giriniz!!!")

    sec = input("Devam etmek için herhangi bir tuşa basınız!!\nÇıkmak için k tuşuna basınız:")
    if (sec == "k" or sec == "K"):
        print("Güle güle  :)))")
        time.sleep(2)
        break
