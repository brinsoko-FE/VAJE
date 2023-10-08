def prva():
    print()

def druga():
    x=2

def tretja():
    x=1
    print(x)
    print(type(x))
    print("---------")
    x=1.2
    print(x)
    print(type(x))

def podatkovni_tipi():
    x=5 #int
    z=5.3 #float
    y=True #bool
    str="blabla" #string

def vpis():
    starost = input("Vpisi starost: ")
    print("Živiš že", starost, "let.")


def komplex_podTipi():
    znamke=["Pes","Mačak","Ovca"]
    print(znamke)
    print("Druga je", znamke[2])

def zivali():
    pets = {
        'macka':'mici',
        'pes':'marjan',
        'slon':'polde'
    }

    print(pets["slon"])

def trikotnik(velikost):
    for i in range(velikost):
        print(" "*(velikost-i),"*"*(i*2+1))


trikotnik(10)


