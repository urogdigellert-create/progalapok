# 1. Adottak a téglalap alapélei. Írassa ki az oldalakat és a kerületet, területet!
a = 5
b = 7
kerulet = 2*(a+b)
terulet = a*b
print("a:",a,"b:",b,"kerület:",kerulet,"terület:",terulet)


# 2. Legyen megadva a kör sugara alapértéknek. Számolja ki a kör átmérőjét, kerületét, területet!
r = 4
pi = 3.14
d = 2*r
k = 2*pi*r
t = pi*r*r
print("r:",r,"d:",d,"k:",k,"t:",t)


# 3.Legyen megadva a háromszög három oldala. Számolja ki a háromszög kerületét, területét
# (héron képlettel)!
a = 3
b = 4
c = 5
kerulet = a+b+c
s = kerulet/2
terulet = (s*(s-a)*(s-b)*(s-c))**0.5
print("a:",a,"b:",b,"c:",c,"kerület:",kerulet,"terület:",terulet)


# 4.Legyen megadva egy szabályos háromszög oldala. Írassa ki a megadott háromszö magasságát!
a = 6
m = (a**2 - (a/2)**2)**0.5
print("a:",a,"m:",m)


# 5.Legyen megadva egy kockának az egyik éle. Írassa ki a lap átló és a test átló hosszát! 
a = 4
lapatl = (2*a**2)**0.5
testatl = (3*a**2)**0.5
print("a:",a,"lapátló:",lapatl,"testátló:",testatl)


# 6.Kérd be külön a vezetéknevet és a keresztnevet, majd összefűzve írasd ki!
vezeteknev = input("Kérem a vezetéknevet: ")
keresztnev = input("Kérem a keresztnevet: ")
print("Név:",vezeteknev,keresztnev)


# 7.Kérjen be egy egész számot! Páros-e a szám? (Oszthatóság vizsgálata: % százék, mint művelet) 
szam = int(input("Kérem az egész számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")


# 8.Segítsd az osztályfőnök munkáját a bizonyítvány íráshoz! Ha az érdemjegy 1,2,3,4,5 - írassa ki 
# szövegesen: 1-elégtelen, 2-elégséges, 3-közepes, 4-jó, 5-jeles. Felhasználó adja meg az 
# érdemjegyet! 
erdemjegy = int(input("Kérem az érdemjegyet (1-5): "))
if erdemjegy == 1:
    print("Érdemjegy: elégtelen")
elif erdemjegy == 2:
    print("Érdemjegy: elégséges")
elif erdemjegy == 3:
    print("Érdemjegy: közepes")
elif erdemjegy == 4:
    print("Érdemjegy: jó")
elif erdemjegy == 5:
    print("Érdemjegy: jeles")
else:
    print("Hibás érdemjegy!")


# 9.Megvan adva a víz hőfoka. Írassa ki, a hőfok alapján hogy szilárd, folyékony, gáz 
# halmazállapotú! 
hofok = float(input("Kérem a víz hőfokát (°C): "))
if hofok < 0:
    print("A víz halmazállapota: szilárd")
elif hofok >= 0 and hofok < 100:
    print("A víz halmazállapota: folyékony")
else:
    print("A víz halmazállapota: gáz")


# 10.Háromszög egyenlőtlenség. Adva van három oldal hossza. Adja meg, hogy szerkeszthető-e a 
# háromszög! HE - akkor szerkeszthető egy háromszög, ha bármely két oldal összege, nagyobb 
# a harmadiknál.
a = float(input("Kérem az első oldal hosszát: "))
b = float(input("Kérem a második oldal hosszát: "))
c = float(input("Kérem a harmadik oldal hosszát: "))
if a+b>c and a+c>b and b+c>a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")


# 11.Adott a hőmérséklet farenheitben. Számolja át cfokba!
f = float(input("Kérem a hőmérsékletet Fahrenheitben: "))
c = (f-32)*5/9
print("A hőmérséklet Celsiusban:",c)


# 12.Adott a hőmérséklet cfokban. Számolja át farenheitbe! 
c = float(input("Kérem a hőmérsékletet Celsiusban: "))
f = c*9/5 + 32
print("A hőmérséklet Fahrenheitben:",f)


# 13.Kérjen be a felhasználótól egy időtávot másodpercben. Számolja át órára, percre, 
# másodpercre! 
masodperc = int(input("Kérem az időtávot másodpercben: "))
ora = masodperc // 3600
perc = (masodperc % 3600) // 60
mp = masodperc % 60
print("Az időtáv:",ora,"óra",perc,"perc",mp,"másodperc")


# HF: Kérjen be a felhasználótól 3 db számot (lehet tört is). Ez a három szám egy háromszög három oldala. 
# 1. Derékszögű-e a háromszög?
# 2. Egyenlőszarú-e a háromszög?
# 3. Szabályos-e a háromszög?

import math
a = float(input("Kérem az első oldal hosszát: "))
b = float(input("Kérem a második oldal hosszát: "))
c = float(input("Kérem a harmadik oldal hosszát: "))
# 1. Derékszögű-e a háromszög?
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("A háromszög derékszögű.")
else:
    print("A háromszög nem derékszögű.")
# 2. Egyenlőszarú-e a háromszög?
if a == b or a == c or b == c:
    print("A háromszög egyenlőszárú.")
else:
    print("A háromszög nem egyenlőszárú.")
# 3. Szabályos-e a háromszög?
if a == b and b == c:
    print("A háromszög szabályos.")
else:
    print("A háromszög nem szabályos.")
# Ellenőrzés, hogy szerkeszthető-e a háromszög
if a+b>c and a+c>b and b+c>a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")


# Generáljon ki három véletlen háromjegyű számot, amelyek 13-al oszthatók! 
# Adja meg az átlaguk!
# Állítsa ezeket sorrendbe!
# Van-e közöttük 4-el végződő?
import random
szam1 = random.randint(100,999)
while szam1 % 13 != 0:
    szam1 = random.randint(100,999)
szam2 = random.randint(100,999)
while szam2 % 13 != 0:
    szam2 = random.randint(100,999)
szam3 = random.randint(100,999)
while szam3 % 13 != 0:
    szam3 = random.randint(100,999)
print("A három szám:",szam1,szam2,szam3)
atlag = (szam1 + szam2 + szam3) / 3
print("Az átlaguk:",atlag)
sorrend = sorted([szam1, szam2, szam3])
print("Sorrendben:",sorrend)
van4elv = False
if szam1 % 10 == 4 or szam2 % 10 == 4 or szam3 % 10 == 4:
    van4elv = True
if van4elv:
    print("Van közöttük 4-el végződő szám.")
else:
    print("Nincs közöttük 4-el végződő szám.")

# páros kétjegyű [5,44]*2 
# 100/13 = 7,6
# 999/13 = 76,8
a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13

szamjegy = int(input("adjon meg egy számjegyet"))

print(a,b,c)

if(a % 10 == szamjegy or b % 10 == szamjegy or c % 10 == szamjegy):
    print("Van közte "+str(szamjegy)+"-re végződő")
else:
    print("Nincs közte "+str(szamjegy)+"-re végződő")


