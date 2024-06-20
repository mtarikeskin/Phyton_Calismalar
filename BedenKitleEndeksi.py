print("""
Beden Kitle Endeksi Hesaplama Programı
""")

kilo = float(input("Kilonuzu giriniz : "))
boy = float(input("Boyunuzu giriniz (santimetre) : "))/100
bki = kilo/(boy**2)

if bki > 30 :
    print("Kategori : Obez")
elif 25 < bki <= 30 :
    print("Kategori : Fazla kilolu")
elif 18.5 < bki <= 25 :
    print("Kategori : Normal")
elif bki <= 18 :
    print("Kategori : Zayıf")
else :
    print("Hata")
