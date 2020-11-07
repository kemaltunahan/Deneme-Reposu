import time

def dene():
    
    global a
    
    a=5
    
    print("a:{}".format(a),"(global)")

dene()

a=10

print("a:",a,"(sonra globalı değiştirdik.)")

time.sleep(2)
