# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")

#kérjen be a felhasznalótól egy számot és mondja meg hogy tizzel odztható e?
# ha nem osztható 10 zel irja ki az utolso szamjegyet
#pl. be: 10 ki: tízzel oszthato
#pl. be: 12 ki: tízzel nem osztható, utolsó száamjegy 2


szam = int(input("Adjon meg egy egész számot:"))
if(szam % 10 == 0):
    print("páros")
else:
    print("páratlan")