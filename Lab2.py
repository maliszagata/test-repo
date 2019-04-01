#Zadanie 1

def suma(x):
    assert len(x)!=0, "Lista jest pusta"
    return sum(x)

def roznica(x):
    assert len(x)!=0, "List is empty"
    y = []
    for i,j in enumerate(x):
        y.append((-1)**i * j)
    return sum(y)
        

def iloczyn(x):
    assert len(x)!=0, "List is empty"
    p = x[0]
    for i in range(1,len(x)):
        p=p*x[i]
    return p
    
#Zadanie 2

def reverse(napis):
    return(napis[::-1])
    
#Zadanie 3

def mirror(napis):
    return napis+napis[::-1]

#Zadanie 4


#Zadanie 5

for i in range(31):
    if i%3!=0:
        print(i)

#Zadanie 6

def rownanie_kw(a,b,c):
    assert a!=0, "To nie jest równanie kwadratowe"
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Brak rozwiązań rzeczywistych"
    elif delta == 0:
        return "Jest jedno rozwiązanie: ", -b/(2*a)
    else:
        return "Są dwa rozwiązania: ", (-b-delta**0.5)/(2*a), (-b+delta**0.5)/(2*a)
    
#Zadanie 7 
        
def pierwsze(n):
    assert n != 0, "Brak"
    p=[]
    for i in range(2,n+1):
        d = 0
        for j in range(1,i+1):
            if i%j==0:
                d+=1
        if d<3:
            p.append(i)
    return(p)

#Zadanie 8

def zdania(tekst):
    Z = tekst.split('. ')
    for i in range(len(Z)):
        W = Z[i].split(" ")
        print(Z[i],", liczba wyrazów: ", len(W))
        
#Zadanie 9
        
def ciag(n,a1=1,q=2):
    return a1*q**(n-1)

#Zadanie 10 

def tabliczka(n):
    for row in range(1, n + 1):
        print(*(f"{row*col:3}" for col in range(1, n + 1)))

def tabliczka1(n):
    for row in range(1,n+1):
        for col in range(1,n+1):
            print(row*col, end="\t")
        print()     

def tabliczka2(n):
    for i in range(1,n+1):
        print(*["{:3}".format(i*j) for j in range(1,n+1)])

#Zadanie 11

def podwojenie(tekst):
    tekst = list(tekst)
    k=0
    for i in range(len(tekst)):
        if (i-k)%2 != 0 and tekst[i]!= " ":
            tekst[i] = tekst[i]*2
        elif tekst[i]==" ":
            k+=1
    for i in range(len(tekst)):
        print(tekst[i],end="")
        

#Zadanie 12
        
def autoryzacja(login, haslo):
    slownik = {
            "Jan":"abcd",
            "Marek":"haslo1",
            "Anna":"admin"}
    if login in slownik and haslo == slownik[login]:
        return "Autoryzacja pomyslna"
    else:
        return "Błąd logowania"

#Przykład:
autoryzacja("Anna","admin")
autoryzacja("Jan","abcd")
autoryzacja("Marek","haslo2")

#Zadanie 13

def rzymskie(liczba):
    rome = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    odp = 0
    i=0
    while i<len(liczba):
        if i!=len(liczba)-1 and rome[liczba[i]] >= rome[liczba[i+1]]:
            odp = odp + rome[liczba[i]]
            i+=1
        elif i!=len(liczba)-1 and rome[liczba[i]] < rome[liczba[i+1]]:
            odp = odp + (rome[liczba[i+1]] - rome[liczba[i]])
            i+=2
        else:
            odp = odp + rome[liczba[i]]
            i+=1
    return odp

#Zadanie 14

def miarka(cm):
    centymetr="|...."
    print(centymetr*cm+"|")
    for i in range(cm+1):
        print(str(i) + "    ", end="")
    
        