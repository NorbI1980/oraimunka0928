def beolvas():
    szam = int(input("Kérem adjon meg egy számot:"))
    return szam
def harom():

    for i in range(0, 21, 1):
        print(i, end=" ")
        #2. megoldás
        for i in range(21):
            print(i)
        #3. megoldás
        for i in range(0, 21):
            print(i)
        #4. megoldás
        i = 0
        while i<21:
            print(i)
            i+=1

def negy():

    for i in range(20,57,2):
        print(i)

def ot():

    for i in range(77,-77,-4):
        print(i)

def hat():

    szam1 = beolvas()
    szam2 = beolvas()
    #melyik a nagyobb
    if szam2 < szam1:
        #csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet
    for i in range(szam1, szam2+1, 1):
        print(i, end=" ")

def het():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        for i in range(0, szorzat-1, -1):
            print(i, end=" ")
    else:
        for i in range(0,szorzat+1, 1):
            print(i, end=" ")

            #HF 8, 9,11, 12
