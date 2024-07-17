

def yazdır(veri) :
    isim, soyisim = veri
    print("{} {}".format(isim,soyisim))

isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler = ["Yılmaz","Keskin","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
zlist = list(zip(isimler,soyisimler))
liste = list(map(yazdır,zlist))
print(liste)















