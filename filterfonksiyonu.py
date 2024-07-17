

def ucgenmi(veri) :
    x,y,z = veri
    if abs(y-z) < x < y+z :
        return True
    else :
        return False

veriler = [(3,4,5),(6,8,10),(3,10,7)]
fliste = list()

liste = list(map(ucgenmi,veriler))
print(liste)
fliste = list(filter(ucgenmi,veriler))
print(fliste)
























