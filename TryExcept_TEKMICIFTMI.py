

def tekmiciftmi(sayi) :

    if sayi.isdigit() != True :
        raise ValueError("Lütfen yalnızca rakamlardan oluşan bir sayı giriniz !!!")
    elif int(sayi) % 2 == 0 :
        print("ÇİFT SAYI !")
    else :
        raise ValueError("Tek sayı hatası !!!")

sayi = input("Lütfen bir sayı giriniz : ")
try :
    tekmiciftmi(sayi)
except ValueError as error:
    print(error)




















