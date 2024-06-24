print("""
***********************
Faktöriyel Bulma Programı

Çıkmak için 'q' tuşlayınız.
***********************
""")

while True :
    sayi = input("Faktöriyelini almak istediğiniz sayıyı giriniz (Çıkmak için 'q' giriniz.) : ")
    if (sayi == "q") :
        print("Program sonlandırılmıştır.")
        break
    else :
        sayi = int(sayi)

        fakt = 1

        for i in range(1,sayi+1) :
            fakt = fakt * i
        print(" Faktöriyel : {}".format(fakt))




















