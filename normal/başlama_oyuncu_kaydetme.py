print("********Oyuncu Kaydetme Programı*******")
while(True):
    ad=input("Adınızı giriniz:")
    soyad=input("Soyadınızı giriniz:")
    takim=input("Takımınızı giriniz:")
    listem=[ad,soyad,takim]
    print("\n**********Bilgiler database içine kaydedildi!!**********")
    print("\nOyuncu Adı:{}\nOyuncu Soyadı:{}\nOyuncu Takımı:{}".format(listem[0],listem[1],listem[2]))
    takim=takim.upper()
    ad=ad.upper()
    print("\n************* {} takımına hosgeldiniz {} BEY ************".format(takim,ad))

    sec=input("Çıkmak için k tusuna basınız")
    if(sec=="k" or sec=="K"):
        break
    
    
