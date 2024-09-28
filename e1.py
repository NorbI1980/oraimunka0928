def elso():
    #1.	A program döntse el, hogy egy egész szám pozitív-e! Először tájékoztassa a felhasználót, hogy mire való a program! Az egész számot a konzolról kérje be! Ha a szám pozitív, akkor ezt írja ki a konzolra, egyébként ne írjon ki semmit!

    szam1 = int(input("Kérem adjon meg egy egész számot!"))
    print(type(szam1))
    if szam1 >0:
        #igaz
        print ("A(z) "+str(szam1)+" pozitív.")