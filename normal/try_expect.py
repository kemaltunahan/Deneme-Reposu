while True:
    
    x = input("Bir sayı girin: ")

    if not x:
        break
    
    try:
        x = 1/float(x)

    except (ValueError):
        print("Geçersiz sayı hatası")
        continue

    except ZeroDivisionError:
        print("Sıfıra bölme hatası")
        continue
    

    print(x)

    
