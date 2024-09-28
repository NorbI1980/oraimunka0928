def husvet():

    ev = int(input("Kéremadjon meg egy évszámot 1900 és 2099 között!"))

    if (ev < 1900) or (ev > 2099):
        print("HIBA nem megfelelő évszám.")
        else:
        m = 24
        n = 5
        a = ev % 19
        b = ev % 4
        c = ev % 7
        d = (19*a + m) % 38
        e = (2*b + 4*c + 6*d + m) % 7
        if (d+e) < 18:
            nap1 = d + e + 22
            print("Húsvét: március" + str(nap1) +"napjára esik.")
        else:
            nap2 = d + e - 9
            if nap2 == 25
                nap2 = 19
            elif nap2 == 26 and (d == 28) and (e == 6) and (a > 10):
                nap2 = 18
                print("Húsvét: április"+ str())
