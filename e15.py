def egeszBeolvas():
    szam = float(input("Kérem adjon meg egy egész számot!"))
    return szam
def teglalap():

   oldal1 = egeszBeolvas()
   oldal2 = egeszBeolvas()

   if (oldal1>0 and oldal2 > 0):
       kerulet = round(2 * (oldal1 + oldal2), 2)
       terulet = round(oldal1 * oldal2, 2)

       print("A téglalap kerülete:" +str(kerulet)+ "területe: " +str(terulet))

   else:
       print("A téglalap oldalai nem pozitívak.")
