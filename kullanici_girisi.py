print("""
*************************
Kullanıcı Girişi Programı
*************************
""")

sys_kullaniciadi = "m.keskintarik"
sys_kullanicisifre = "KeskinTarik123"
girishakki = 3

while True :
    kullaniciadi = input("Kullanıcı Adı : ")
    kullanicisifre = input("Kullanıcı Şifre : ")

    if (kullaniciadi != sys_kullaniciadi or kullanicisifre != sys_kullanicisifre ) :
        girishakki = girishakki - 1
        print("Kullanıcı adı veya şifre hatalıdır. Kalan deneme hakkı : {}".format(girishakki))
    else :
        print("Giriş yapılıyor...")
        break
    if (girishakki == 0) :
        print("Giriş hakkınız dolmuştur daha sonra tekrar deneyiniz.")
        break











