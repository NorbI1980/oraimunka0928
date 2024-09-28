def fmasodik():
#A program olvasson be a konzolról egy egész számot! A program döntse el, hogy a megadott számpáros vagy páratlan, és írja ki az eredményt a konzolra!
szam = int(input("Kérem adjon meg egy egész számot!"))
    if szam%2 == 0:
        print("A szám páros")
    else:
        print("A szám páratlan")