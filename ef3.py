def fharom():
    #A program  olvasson be a konzolról egy valós számot! A program számítsa ki a szám abszolút értékét, és írja ki az eredményeket a konzolra! A számításhoz a math.fabs() függvény helyett elágazást használjon!
    szam = float(input("Kérem adjon meg egy egész számot!"))
    if szam >= 0:
        eredmeny = szam
        print("|"+str(szam) + "|" + str(eredmeny))
    else:
        eredmeny = szam * (-1)
        print("|"+ str(szam)+ "|" + str(eredmeny))