print("""
********************
Sonsuz Toplam Programı

Programı sonlandırmak için 'q' tuşlayınız.
********************
""")

toplam = 0

while True :
    sayi = input("Lütfen bir sayı giriniz : ")
    if (sayi.lower() == "q") :
        break
    else :
        sayi = int(sayi)
        toplam = toplam + sayi
print("Toplam = {}".format(toplam))

































