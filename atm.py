print("""
***************************
Hoşgeldiniz...

Bakiye Sorgulama için 1
Para Yatırma için 2
Para çekme için 3 tuşlayınız.
Çıkış yapmak için 0'ı tuşlayınız.
***************************
""")

bakiye = 1000

while True :
    islem = input("İşlemi seçiniz : ")
    if (islem == "0") :
        print("Çıkış yapılıyor...")
        break
    elif (islem == "1") :
        print("Bakiyeniz {} TL'dir.".format(bakiye))
    elif (islem == "2") :
        yatirilantutar = int(input("Yatırmak istediğiniz tutarı giriniz : "))
        bakiye = bakiye + yatirilantutar
        print("Para yatırma işleminiz gerçekleştirilmiştir. Güncel bakiye : {}".format(bakiye))
    elif (islem == "3") :
        cekilentutar = int(input("Çekmek istediğiniz tutarı giriniz : "))
        if (cekilentutar > bakiye) :
            print("Çekmek istediğiniz tutar için bakiyeniz yetersizdir.")
            continue # Burada continue kullanarak eğer çekilmek istenen tutar bakiyeden büyükse alt satırlarda yer alan bakiyeden
            #çekilen tutarı eksiltme işlemini programama yaptırtmıyoruz ve programı en başa yolluyoruz.
        bakiye = bakiye - cekilentutar
        print("Para çekme işleminiz gerçekleştirilmiştir."
              "Güncel bakiye : {}".format(bakiye))
    else :
        print("Geçersiz tuşlama yaptınız.")














