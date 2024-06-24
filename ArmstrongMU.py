print("""
*********************
Armstrong Mu?

Programı sonlandırmak için 'x' tuşlayınız.
*********************
""")

toplam = 0

while True :
    sayi = input("Bir sayı giriniz : ")
    if (sayi == "x") :
        print("Program sonlandırıldı.")
        break
    else :
        sayi = list(sayi)
        for i in range(0, len(sayi)) :
            toplam = toplam + int(sayi[i])**len(sayi)
        print(toplam)
        joinedsayi = ''.join(sayi)
        intsayi = int(joinedsayi)
        if (intsayi == toplam) :
            print("Girdiğini sayı bir ARMSTRONG SAYISIDIR.")
        else :
            print("Girdiğiniz sayı bir ARMSTRONG SAYISI DEĞİLDİR.")





























