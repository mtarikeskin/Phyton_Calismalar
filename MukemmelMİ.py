

def mukemmelmi(x) :
    toplam = 0
    for i in range(1,x) :
        if x % i == 0 :
            toplam = toplam + i
    if toplam == x :
        return True
    else :
        return False

while True :
    sayi = input("Lütfen mükemmelliğini sorgulamak istediğiniz sayıyı giriniz (Çıkmak için q basınız.) : ")
    if sayi.lower() == "q" :
        print("Program sonlandırıldı.")
        break
    else :
        sayi = int(sayi)
        if mukemmelmi(sayi) :
            print("Girdiğiniz sayı MÜKEMMELDİR.")
        else :
            print("Girdiğiniz sayı MÜKEMMEL DEĞİLDİR.")

