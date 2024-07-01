

def pisagor() :
    for a in range(1,101) :
        for b in range(1,101) :
            ckare = a**2 + b**2
            c = ckare**0.5
            if (c >= 0 and c <= 100) and c.is_integer() :
                print("a = {} b = {} c = {}".format(a,b,c))

pisagor()






