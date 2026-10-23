"""
byer = []
byer.append("Oslo")
byer.append("Bergen")
byer.append("Trondheim")
byer.append("Stavanger")
print(byer)
print(len(byer))


"""
"""
frukt = ["eple", "banan", "appelsin"]
frukt[1] = "kiwi"
frukt.append("druer")
print(frukt)


"""
"""
tall = [5, 10, 15, 20, 25, 30]
tall.remove(15)
tall.pop()
print(tall)
print(len(tall))


"""
"""
hobbyer = []

for i in range(3):
    hobby = input("Skriv inn en hobby: ")
    hobbyer.append(hobby)

print("Dine hobbyer er:", hobbyer)


"""
"""
land = ["Norge", "Sverige", "Danmark", "Finland"]
svar = input("Skriv inn et land: ").lower()

if svar in [l.lower() for l in land]:
    print("Landet finnes i listen")
else:
    print("Landet finnes ikke i listen")


"""
"""
bokstaver = ["a", "b", "a", "c", "a", "b", "a"]
bokstav = input("Skriv inn en bokstav: ")
print("Antall ganger:", bokstaver.count(bokstav))


"""
"""
opprinnelig = [1, 3, 5, 7, 9]
doblet = []

for tall in opprinnelig:
    doblet.append(tall * 2)

print(opprinnelig)
print(doblet)


"""
"""
poeng = []
antall = int(input("Hvor mange poeng vil du registrere? "))

for i in range(antall):
    verdi = int(input("Skriv inn poeng: "))
    poeng.append(verdi)

print(poeng)

if len(poeng) > 0:
    print(max(poeng))


"""
"""
ord = ["hus", "bil", "datamaskin", "bok", "dvd-spiller", "penn"]
lange_ord = []

for tekst in ord:
    if len(tekst) > 5:
        lange_ord.append(tekst)

print(lange_ord)


"""
"""
navn = []
telefon = []

antall = int(input("Hvor mange kontakter? "))

for i in range(antall):
    navn.append(input("Navn: "))
    telefon.append(input("Telefonnummer: "))

for i in range(len(navn)):
    print(navn[i], "-", telefon[i])


"""
"""
temperaturer = []

for i in range(7):
    temp = float(input("Skriv inn temperatur: "))
    temperaturer.append(temp)

print("Gjennomsnitt:", sum(temperaturer) / len(temperaturer))
print("Høyeste:", max(temperaturer))
print("Laveste:", min(temperaturer))

over_15 = 0

for temp in temperaturer:
    if temp > 15:
        over_15 += 1

print("Dager over 15 grader:", over_15)


"""
"""
rot = [1, "hei", 2, "ha det", 3, "morgen", 4]
tall_liste = []
tekst_liste = []

for element in rot:
    if type(element) == int:
        tall_liste.append(element)
    elif type(element) == str:
        tekst_liste.append(element)

print(tall_liste)
print(tekst_liste)


"""
"""
varer = []

while True:
    print("1. Vis varer")
    print("2. Legg til vare")
    print("3. Fjern vare")
    print("4. Søk etter vare")
    print("5. Tell varer")
    print("6. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        print(varer)
    elif valg == "2":
        varer.append(input("Ny vare: "))
    elif valg == "3":
        vare = input("Vare som skal fjernes: ")
        if vare in varer:
            varer.remove(vare)
        else:
            print("Varen finnes ikke")
    elif valg == "4":
        vare = input("Søk etter vare: ")
        if vare in varer:
            print("Varen finnes")
        else:
            print("Varen finnes ikke")
    elif valg == "5":
        print("Antall varer:", len(varer))
    elif valg == "6":
        break


"""
"""
karakterer = []

while True:
    karakter = input("Skriv karakter (A-F) eller ferdig: ").upper()

    if karakter == "FERDIG":
        break

    if karakter in ["A", "B", "C", "D", "E", "F"]:
        karakterer.append(karakter)
    else:
        print("Ugyldig karakter")

for k in ["A", "B", "C", "D", "E", "F"]:
    print(k, ":", karakterer.count(k))

if len(karakterer) > 0:
    mest_vanlig = max(["A", "B", "C", "D", "E", "F"], key=karakterer.count)
    print("Mest vanlige:", mest_vanlig)

    antall_ab = karakterer.count("A") + karakterer.count("B")
    print("Prosent A eller B:", antall_ab / len(karakterer) * 100)


"""
"""
tall = []

while True:
    svar = input("Skriv et tall eller stopp: ")

    if svar.lower() == "stopp":
        break

    tall.append(int(svar))

print("Alle tall:", tall)
print("Antall tall:", len(tall))

if len(tall) > 0:
    print("Sum:", sum(tall))
    print("Gjennomsnitt:", sum(tall) / len(tall))

    partall = []
    oddetall = []

    for t in tall:
        if t % 2 == 0:
            partall.append(t)
        else:
            oddetall.append(t)

    print("Partall:", partall)
    print("Oddetall:", oddetall)


"""
"""
norsk = []
engelsk = []

def slå_opp(ord):
    if ord in norsk:
        indeks = norsk.index(ord)
        print(engelsk[indeks])
    else:
        print("Ordet finnes ikke")

while True:
    print("1. Legg til ord")
    print("2. Slå opp ord")
    print("3. Test deg selv")
    print("4. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        norsk.append(input("Norsk ord: "))
        engelsk.append(input("Engelsk ord: "))
    elif valg == "2":
        slå_opp(input("Skriv norsk ord: "))
    elif valg == "3":
        if len(norsk) > 0:
            indeks = int(input("Velg ordnummer fra 0 til " + str(len(norsk) - 1) + ": "))
            if 0 <= indeks < len(norsk):
                svar = input("Hva er " + norsk[indeks] + " på engelsk? ")
                if svar.lower() == engelsk[indeks].lower():
                    print("Riktig!")
                else:
                    print("Feil! Riktig svar er", engelsk[indeks])
    elif valg == "4":
        break


"""
"""
beregninger = []

while True:
    print("1. Regn ut")
    print("2. Vis historikk")
    print("3. Slett historikk")
    print("4. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        a = float(input("Første tall: "))
        b = float(input("Andre tall: "))
        tegn = input("Velg +, -, * eller /: ")

        if tegn == "+":
            resultat = a + b
        elif tegn == "-":
            resultat = a - b
        elif tegn == "*":
            resultat = a * b
        elif tegn == "/" and b != 0:
            resultat = a / b
        else:
            print("Ugyldig operasjon")
            continue

        tekst = str(a) + " " + tegn + " " + str(b) + " = " + str(resultat)
        beregninger.append(tekst)
        print(tekst)

    elif valg == "2":
        print(beregninger)
    elif valg == "3":
        beregninger.clear()
    elif valg == "4":
        break


"""
"""
liste = []

while True:
    print("1. Lag liste")
    print("2. Vis liste")
    print("3. Legg til tall")
    print("4. Fjern tall")
    print("5. Reverser liste")
    print("6. Sorter liste")
    print("7. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        liste = []
        antall = int(input("Hvor mange tall? "))
        for i in range(antall):
            liste.append(int(input("Tall: ")))
    elif valg == "2":
        print(liste)
    elif valg == "3":
        indeks = int(input("Posisjon: "))
        verdi = int(input("Tall: "))
        liste.insert(indeks, verdi)
    elif valg == "4":
        indeks = int(input("Posisjon som skal fjernes: "))
        if 0 <= indeks < len(liste):
            liste.pop(indeks)
        else:
            print("Ugyldig posisjon")
    elif valg == "5":
        liste.reverse()
        print(liste)
    elif valg == "6":
        liste.sort()
        print(liste)
    elif valg == "7":
        break


"""
"""
mine_tall = [1, 2, 3]
mine_tall.append(4)
print(mine_tall)


"""
"""
farger = ["rød", "blå", "grønn"]

if "gul" in farger:
    farger.remove("gul")

print(farger)


"""
"""
dyr = ["hund", "katt", "fugl"]
print(dyr[2])


"""
"""
tall = [10, 20, 30]
fjernet = tall.pop(2)
print(fjernet)


"""
"""
varer = []
priser = []

while True:
    print("1. Legg til vare")
    print("2. Vis handleliste")
    print("3. Fjern vare")
    print("4. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        varer.append(input("Vare: "))
        priser.append(float(input("Pris: ")))
    elif valg == "2":
        total = 0
        for i in range(len(varer)):
            print(varer[i], "-", priser[i], "kr")
            total += priser[i]
        print("Totalpris:", total, "kr")
    elif valg == "3":
        vare = input("Hvilken vare vil du fjerne? ")
        if vare in varer:
            indeks = varer.index(vare)
            varer.pop(indeks)
            priser.pop(indeks)
        else:
            print("Varen finnes ikke")
    elif valg == "4":
        break


"""
"""
import random

sanger = ["Sang 1", "Sang 2", "Sang 3", "Sang 4"]
random.shuffle(sanger)

for i in range(len(sanger)):
    print("Nå spiller:", sanger[i])

    if i + 1 < len(sanger):
        print("Neste sang:", sanger[i + 1])
    else:
        print("Ingen flere sanger")


"""
"""
oppgaver = []
ferdig = []

while True:
    print("1. Legg til oppgave")
    print("2. Vis oppgaver")
    print("3. Marker som ferdig")
    print("4. Avslutt")

    valg = input("Velg: ")

    if valg == "1":
        oppgaver.append(input("Skriv oppgave: "))
        ferdig.append(False)
    elif valg == "2":
        for i in range(len(oppgaver)):
            if ferdig[i]:
                print("V", oppgaver[i])
            else:
                print("X", oppgaver[i])
    elif valg == "3":
        indeks = int(input("Nummer på oppgave: "))
        if 0 <= indeks < len(oppgaver):
            ferdig[indeks] = True
        else:
            print("Ugyldig nummer")
    elif valg == "4":
        break
    """