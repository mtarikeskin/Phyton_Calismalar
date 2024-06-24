print("""
*******************************
Bir Sayının Mükemmel Sayı Olup Olmadığını Bulma Programı

Programdan çıkmak için x tuşlayınız.
*******************************
""")

mukemmellik = 0

while True :
    sayi = input("Lütfen mükemmelliğini sorgulamak istediğiniz sayıyı giriniz : ")
    if(sayi == "x") :
        print("Program sonladırıldı.")
        break
    else :
        sayi = int(sayi)
        for i in range(1,sayi) :
            if(sayi%i == 0) :
                mukemmellik = mukemmellik + i
        if mukemmellik == sayi :
            print("Girdiğiniz sayı MÜKEMMELDİR.")
            mukemmellik = 0
        else :
            print("Girdiğiniz sayı MÜKEMMEL DEĞİLDİR.")
            mukemmellik = 0

























