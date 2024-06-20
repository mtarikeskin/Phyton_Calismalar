print("""
En Büyük Sayıyı Ekrana Yazdırma Programı
""")

sayi1 = int(input("Lütfen 1. sayıyı giriniz : "))
sayi2 = int(input("Lütfen 2. sayıyı giriniz : "))
sayi3 = int(input("Lütfen 3. sayıyı giriniz : "))

if sayi1 > sayi2 and sayi1 > sayi3 :
    print("En büyük sayı {}'dir.".format(say1))
elif sayi2 > sayi1 and sayi2 > sayi3 :
    print("En büyük sayı {}'dir.".format(sayi2))
elif sayi3 > sayi1 and sayi3 > sayi2 :
    print("En büyük sayı {}'dir.".format(sayi3))
else :
    print("Bir hata meydana geldi.")








