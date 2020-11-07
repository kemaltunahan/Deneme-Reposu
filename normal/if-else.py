import time
kayitli="kemal"
sifre="1310"
bool=True 

while(True):
    kaydol=input("Kullanıcı adınızı girin:")
    parola=input("Parolanızı giriniz:")

    if ((kayitli==kaydol) and (sifre==parola)):
        print("Sisteme hoşgeldiniz!!")
        print("işlem seçiniz:")
        time.sleep(2)
        break

    elif ((kayitli==kaydol) and (sifre!=parola)):
        print("Parolanız yanlış!!")
        print("Tekrar deneyiniz!!")

    elif ((kayitli!=kaydol) and (sifre==parola)):
        print("Kullanıcı adınız yanlış!!")
        print("Tekrar deneyiniz!!")

    else:
        print("Tekrar deneyiniz!!")

