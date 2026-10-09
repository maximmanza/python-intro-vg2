"""
handleliste = []
while True:
    vare = input("Skriv inn en vare (eller 'q' for å avslutte): ")
    if vare.lower() == "q":
        break
    handleliste.append(vare)
print("Handleliste:", handleliste)

"""
"""

sum_tall = 0
antall = 0
while True:
    svar = input("Skriv inn et tall (eller 'q' for å avslutte): ")
    if svar.lower() == "q":
        break
    sum_tall += int(svar)
    antall += 1
print("Sum:", sum_tall)
print("Antall tall:", antall)
"""
"""

nummer = [5, -2, 9, 0, 7, -3, 4]
positive = [x for x in nummer if x > 0]
print("Positive tall:", positive)

"""
"""

karakterer = ["A", "B", "B", "C", "A", "A", "D", "B"]
statistikk = {}
for karakter in karakterer:
    statistikk[karakter] = statistikk.get(karakter, 0) + 1
print("Karakterstatistikk:", statistikk)

"""
"""
passord = input("Skriv inn et passord: ")
if len(passord) >= 6:
    print("Gyldig passord")
else:
    print("Passordet er for kort")

"""
"""

import random
hemmelig_tall = random.randint(1, 10)
while True:
    gjett = int(input("Gjett et tall mellom 1 og 10: "))
    if gjett == hemmelig_tall:
        print("Riktig! Du gjettet riktig.")
        break
    print("Feil, prøv igjen.")

"""
"""

alder = 18
if alder >= 18:
    print("Du er myndig")
else:
    print("Du er ikke myndig")

"""
"""
for i in range(1, 6):
    print(i)

# Oppgave 19: Logikk-feil
poeng = 85
if poeng >= 80:
    print("Godt jobbet!")
else:
    print("Prøv igjen")

"""
"""

teller = 0
while teller < 5:
    print(teller)
    teller += 1

"""
"""

for i in range(1, 6):
    print("*" * i)

"""
"""

antall = 10
a, b = 0, 1
for _ in range(antall):
    print(a, end=" ")
    a, b = b, a + b
print()

"""
"""

ordbank = []
for i in range(3):
    ord = input(f"Skriv inn ord {i + 1}: ")
    ordbank.append(ord)
print("Ordbank:", ordbank)

"""
"""

poengsum = 0
for i in range(5):
    poeng = int(input(f"Skriv inn poeng {i + 1}: "))
    poengsum += poeng
print("Totalt antall poeng:", poengsum)

"""
"""

print("   /\\")
print("  /  \\")
print("  |  |")
print("  /_\\")
print(" /___\\")
print("/_____|\\")
print("  || ||")

"""
"""

for i in range(1, 4):
    print(" " * (3 - i) + "/" + " " * (2 * i - 2) + "\\")
print("/___\\")
print("|   |")
print("|_|_|")

"""
