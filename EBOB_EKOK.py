

def ebob(sayi1,sayi2) :
    if sayi1 > sayi2 :
        while sayi2 != 0 :
            sayi1,sayi2 = sayi2,sayi1 % sayi2
        return sayi1
    else :
        sayi1,sayi2 = sayi2,sayi1
        while sayi1 != 0 :
            sayi2,sayi1 = sayi1,sayi2 % sayi1
        return sayi2

def ekok(sayi1,sayi2) :
    if sayi1 > sayi2 :
        carpim = sayi1*sayi2
        while sayi2 != 0 :
            sayi1,sayi2 = sayi2,sayi1 % sayi2
        ekok = carpim/sayi1
        return ekok
    else :
        sayi1,sayi2 = sayi2,sayi1
        carpim = sayi1*sayi2
        while sayi1 != 0 :
            sayi2,sayi1 = sayi1,sayi2 % sayi1
        ekok = carpim/sayi2
        return ekok



while True :
    sayi1 = input("Lütfen EBOB-EKOK'unu bulmak istediğiniz 1. sayıyı giriniz (Çıkmak için 'q' giriniz.) : ")
    sayi2 = input("Lütfen EBOB-EKOK'unu bulmak istediğiniz 2. sayıyı giriniz (Çıkmak için 'q' giriniz.) : ")
    if sayi1.lower() == "q" or sayi2.lower() == "q" :
        print("Program sonlandırıldı.")
        break
    else :
        sayi1 = int(sayi1)
        sayi2 = int(sayi2)
        print("EBOB = {0}\tEKOK = {1}".format(ebob(sayi1,sayi2),ekok(sayi1,sayi2)))

