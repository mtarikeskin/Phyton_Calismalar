print("""
Geometrik Şekil Bulma Programı

Dikdörtgen için 1
Üçgen için 2 giriniz.

""")
secim = int(input("Lütfen bir geometrik şekil giriniz : "))

if secim == 1 :
    d1 = int(input("d1 uzunluğunu giriniz : "))
    d2 = int(input("d2 uzunluğunu giriniz : "))
    d3 = int(input("d3 uzunluğunu giriniz : "))
    d4 = int(input("d4 uzunluğunu giriniz : "))
    d1 = abs(d1)
    d2 = abs(d2)
    d3 = abs(d3)
    d4 = abs(d4)
    if d1 == d2 == d3 == d4 :
        print("Ölçülerini girdiğiniz dörtgen bir karedir.")
    elif d1 == d2 and d3 == d4 :
        print("Ölçülerini girdiğiniz dörtgen bir dikdörtgendir.")
    elif d1 == d3 and d2 == d4 :
        print("Ölçülerini girdiğiniz dörtgen bir dikdörtgendir.")
    elif d1 == d4 and d2 == d3 :
        print("Ölçülerini girdiğiniz dörtgen bir dikdörtgendir.")
    else :
        print("Ölçülerini girdiğiniz dörtgen özel bir dörtgen değildir.")
elif secim ==2 :
    u1 = int(input("u1 uzunluğunu giriniz : "))
    u2 = int(input("u2 uzunluğunu giriniz : "))
    u3 = int(input("u3 uzunluğunu giriniz : "))
    u1 = abs(u1)
    u2 = abs(u2)
    u3 = abs(u3)
    if abs(u2 - u3) < u1 < (u2+u3) or  abs(u3 - u1) < u2 < (u3+u1) or abs(u2 - u1) < u3 < (u2+u1) :
        if u1 == u2 == u3 :
            print("Ölçülerini girdiğiniz üçgen eşkenar bir üçgendir.")
        elif u1 == u2 or u1 == u3 or u2 == u3 :
            print("Ölçülerini girdiğiniz üçgen ikizkenar bir üçgendir.")
        else :
            print("Ölçülerini girdiğiniz üçgen özel bir üçgen değildir.")
    else :
       print("Girdiğiniz ölçüler üçgen oluşturmamaktadır.")
else :
    print("Hatalı bir seçim yaptınız !")







