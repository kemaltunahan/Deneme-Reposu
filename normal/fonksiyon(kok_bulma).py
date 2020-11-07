import time
def kokbul(a,b,c):
    delta=b**2-4*a*c

    if(delta<0):
        return("Reel kök yoktur!!")

    else:
        x1=int((-b-delta**0.5)/2*a)
        x2=int((-b-delta**0.5)/2*a)

        return(x1,x2) 
while(True):
    a=int(input("a:"))
    b=int(input("b:"))
    c=int(input("c:"))

    sonuc=kokbul(a,b,c)
    print(sonuc)

