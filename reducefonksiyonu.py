from functools import reduce

def ciftmi(veri) :
    if veri % 2 == 0 :
        return True
    else :
        return False


veriler = [1,2,3,4,5,6,7,8,9,10]

fliste = list(filter(ciftmi,veriler))
print(fliste)

toplam = reduce(lambda x,y : x + y, fliste)
print(toplam)




















