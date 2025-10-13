szam = int(input("Adjon meg egy egész számot:"))
if(szam % 10 == 0):
    print("tízzel osztható")
else:
    print("tízzel nem osztható")
    print("az utolsó számjegy: " + str(szam % 10))

# Kérjen be egy masik szamot és irassa ki a két szám reciprokának összegét!

szam = int(input("Adjon meg egy egész számot: "))
if (szam % 10 == 0):
    print("Tízzel osztható")
else:
    print("Tízzel nem osztható")
    print("Az utolsó számjegy: " + str(szam % 10))

masik_szam = int(input("Adjon meg egy másik egész számot: "))

if (szam == 0 or masik_szam == 0):
    print("Nem lehet nullának venni a reciprokát!")
else:
    reciprok_osszeg = 1 / szam + 1 / masik_szam
    print("A két szám reciprokának összege:", reciprok_osszeg)

# Két szám összegének a gyöke

osszeg = szam + masik_szam
if osszeg < 0:
    print("Negatív számnak nincs gyöke!")
else:
    from math import sqrt
    gyok = sqrt(osszeg)
    print("A két szám összegének a gyöke:", gyok)
