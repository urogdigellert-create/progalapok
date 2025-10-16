# -----------------------------
# 1️⃣ Téglalap adatok
# -----------------------------
a = 5
b = 7
kerulet = 2*(a+b)  # kerület = 2*(a+b)
terulet = a*b       # terület = a*b
print("Téglalap a:",a,"b:",b,"kerület:",kerulet,"terület:",terulet)

# -----------------------------
# 2️⃣ Kör adatai
# -----------------------------
r = 4
pi = 3.14
d = 2*r         # átmérő
k = 2*pi*r      # kerület
t = pi*r*r      # terület
print("Kör r:",r,"d:",d,"k:",k,"t:",t)

# -----------------------------
# 3️⃣ Háromszög Heron képlettel
# -----------------------------
a = 3
b = 4
c = 5
kerulet = a+b+c
s = kerulet/2
terulet = (s*(s-a)*(s-b)*(s-c))**0.5  # Heron képlet
print("Háromszög a:",a,"b:",b,"c:",c,"kerület:",kerulet,"terület:",terulet)

# -----------------------------
# 4️⃣ Szabályos háromszög magassága
# -----------------------------
a = 6
m = (a**2 - (a/2)**2)**0.5
print("Szabályos háromszög a:",a,"magasság:",m)

# -----------------------------
# 5️⃣ Kocka átlók
# -----------------------------
a = 4
lapatl = (2*a**2)**0.5   # lapátló
testatl = (3*a**2)**0.5  # testátló
print("Kocka a:",a,"lapátló:",lapatl,"testátló:",testatl)

# -----------------------------
# 6️⃣ Név bekérése
# -----------------------------
vezeteknev = input("Kérem a vezetéknevet: ")
keresztnev = input("Kérem a keresztnevet: ")
print("Név:",vezeteknev,keresztnev)

# -----------------------------
# 7️⃣ Páros vagy páratlan szám
# -----------------------------
szam = int(input("Kérem az egész számot: "))
if szam % 2 == 0:
    print("A szám páros.")
else:
    print("A szám páratlan.")

# -----------------------------
# 8️⃣ Érdemjegy szövegesen
# -----------------------------
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

# -----------------------------
# 9️⃣ Víz halmazállapota
# -----------------------------
hofok = float(input("Kérem a víz hőfokát (°C): "))
if hofok < 0:
    print("A víz halmazállapota: szilárd")
elif 0 <= hofok < 100:
    print("A víz halmazállapota: folyékony")
else:
    print("A víz halmazállapota: gáz")

# -----------------------------
# 10️⃣ Háromszög szerkeszthetőség
# -----------------------------
a = float(input("Kérem az első oldal hosszát: "))
b = float(input("Kérem a második oldal hosszát: "))
c = float(input("Kérem a harmadik oldal hosszát: "))
if a+b>c and a+c>b and b+c>a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")

# -----------------------------
# 11️⃣ Fahrenheit → Celsius
# -----------------------------
f = float(input("Kérem a hőmérsékletet Fahrenheitben: "))
c = (f-32)*5/9
print("A hőmérséklet Celsiusban:",c)

# -----------------------------
# 12️⃣ Celsius → Fahrenheit
# -----------------------------
c = float(input("Kérem a hőmérsékletet Celsiusban: "))
f = c*9/5 + 32
print("A hőmérséklet Fahrenheitben:",f)

# -----------------------------
# 13️⃣ Másodperc → óra, perc, mp
# -----------------------------
masodperc = int(input("Kérem az időtávot másodpercben: "))
ora = masodperc // 3600
perc = (masodperc % 3600) // 60
mp = masodperc % 60
print("Az időtáv:",ora,"óra",perc,"perc",mp,"másodperc")

# -----------------------------
# HF: Háromszög típusok
# -----------------------------
import math
a = float(input("Kérem az első oldal hosszát: "))
b = float(input("Kérem a második oldal hosszát: "))
c = float(input("Kérem a harmadik oldal hosszát: "))

# Derékszögű?
if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("A háromszög derékszögű.")
else:
    print("A háromszög nem derékszögű.")

# Egyenlőszárú?
if a == b or a == c or b == c:
    print("A háromszög egyenlőszárú.")
else:
    print("A háromszög nem egyenlőszárú.")

# Szabályos?
if a == b and b == c:
    print("A háromszög szabályos.")
else:
    print("A háromszög nem szabályos.")

# Szerkeszthetőség
if a+b>c and a+c>b and b+c>a:
    print("A háromszög szerkeszthető.")
else:
    print("A háromszög nem szerkeszthető.")

# -----------------------------
# Véletlen háromjegyű számok 13-mal osztható
# -----------------------------
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

print("A három szám:", szam1, szam2, szam3)

atlag = (szam1 + szam2 + szam3)/3
print("Az átlaguk:", atlag)

sorrend = sorted([szam1, szam2, szam3])
print("Sorrendben:", sorrend)

van4elv = False
if szam1 % 10 == 4 or szam2 % 10 == 4 or szam3 % 10 == 4:
    van4elv = True

if van4elv:
    print("Van közöttük 4-el végződő szám.")
else:
    print("Nincs közöttük 4-el végződő szám.")

# -----------------------------
# Páros, kétjegyű számok 13-mal osztható
# -----------------------------
a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13

szamjegy = int(input("Adjon meg egy számjegyet: "))

print(a,b,c)

if a%10 == szamjegy or b%10 == szamjegy or c%10 == szamjegy:
    print("Van közte "+str(szamjegy)+"-re végződő")
else:
    print("Nincs közöttük "+str(szamjegy)+"-re végződő")
