

def sayininokunusu(sayi) :
    okunus1 = ["sıfır","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

    if sayi >= 0 and sayi < 10 :
        for i in range(0,10) :
            if sayi == i :
                print(okunus1[i])
    elif sayi >= 10 and sayi < 20 :
        for i in range(10,20) :
            if sayi == i :
                i = i - 10
                print("on {}".format(okunus1[i]))
    elif sayi >= 20 and sayi < 30 :
        for i in range(20,30) :
            if sayi == i :
                i = i - 20
                print("yirmi {}".format(okunus1[i]))
    elif sayi >= 30 and sayi < 40 :
        for i in range(30,40) :
            if sayi == i :
                i = i - 30
                print("otuz {}".format(okunus1[i]))
    elif sayi >= 40 and sayi < 50 :
        for i in range(40,50) :
            if sayi == i :
                i = i - 40
                print("kırk {}".format(okunus1[i]))
    elif sayi >= 50 and sayi < 60 :
        for i in range(50,60) :
            if sayi == i :
                i = i - 50
                print("elli {}".format(okunus1[i]))
    elif sayi >= 60 and sayi < 70 :
        for i in range(60,70) :
            if sayi == i :
                i = i - 60
                print("altmış {}".format(okunus1[i]))
    elif sayi >= 70 and sayi < 80 :
        for i in range(70,80) :
            if sayi == i :
                i = i - 70
                print("yetmiş {}".format(okunus1[i]))
    elif sayi >= 80 and sayi < 90 :
        for i in range(80,90) :
            if sayi == i :
                i = i - 80
                print("seksen {}".format(okunus1[i]))
    elif sayi >= 90 and sayi < 100 :
        for i in range(90,100) :
            if sayi == i :
                i = i - 90
                print("doksan {}".format(okunus1[i]))
    else :
        print("Lütfen 0-100 arası bir sayı giriniz !!!")

while True :
    sayi = input("Lütfen bir 0-100 arası sayı giriniz (Çıkmak için 'q' tuşlayınız.) : ")
    if sayi.lower() == "q" :
        print("Program sonlandırıldı.")
        break
    else :
        sayi = int(sayi)
        sayininokunusu(sayi)
