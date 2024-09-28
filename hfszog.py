def szog()

    vSzam = float(input("Kérem adjon meg egy valós számot!"))
    if (vSzam >= 0) and (vSzam <= 360):
        if vSzam == 0:
            print(str(vSzam)+" --> nullaszög")
        elif (vSzam>0) and (vSzam<90):
            print(srt(vSzam)+" --> hegyesszog")
            elif (vSzam > 0) and (vSzam < 90):
            print(srt(vSzam) + " --> hegyesszog")
            elif (vSzam == 0) and (vSzam < 90):
            print(srt(vSzam) + " --> hegyesszog")