import time
def hesap(yas):
    if yas == 0:
        return 0
    else:
        return 365 + hesap(yas-1)

x = int(input("Yaşınızı giriniz: "))
print (hesap(x),"gündür hayattasın!!")

time.sleep(2)
