4.	Osztályzat2: A program beolvas a konzolról egy egész számot!
Ha a szám 1 és 5 közötti, akkor legyen a beolvasott szám egy osztályzat!
A program írja ki a konzolra a számmal megadott osztályzatot szövegesen (1=elégtelen, …, 5=jeles)!
Ha a szám nem 1 és 5 közötti, akkor a program írja ki konzolra, hogy „érvénytelen osztályzat”!
szam = int(input("Kérem adjon meg egy osztályzatot!"))
if szam >= 1 and szam <=5:
    if szam == 1:
        print("elégtelen")
        if szam == 2:
            print("elégséges")
            if szam == 3:
                print("közepes")
                if szam == 4:
                    print("jó")
                    else:
                        print("jeles")
                else:
                    print("Érvénytelen osztályzat!")