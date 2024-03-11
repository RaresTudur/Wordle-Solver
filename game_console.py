import random
import os
from termcolor import colored

numar_incercari = 0
cuvinte_incercate = []


def ghicire(raspuns_corect,cuvant_incercat):
    pozitie = 0
    global hint
    hint = ""
    cuvant = []
    for l in cuvant_incercat:
        if l == raspuns_corect[pozitie]:
            hint += "C"
            cuvant.append(colored(l,'green'))
        elif l in raspuns_corect:
            hint += "E"
            cuvant.append(colored(l,'yellow'))
        else:
            hint += "-"
            cuvant.append(colored(l,'grey'))
        pozitie += 1
    cuvant = " ".join(cuvant)
    cuvinte_incercate.append(cuvant)
    return hint == "CCCCC"

def interfata(total,marime: int = 9, pad: int = 1):
    marime_interfata = marime + pad * 2
    bara_sus = "┏" + "━" * marime_interfata + "┓"
    spatiu = " " * pad
    print(bara_sus)
    for cuvant in total:
        print("┃" + spatiu + cuvant + spatiu + "┃")
    bara_jos = "┗" + "━" * marime_interfata + "┛"
    print(bara_jos + "\n")
    

def afisare(cuvinte_incercate: list[str]):
    total = []
    for cuvant in cuvinte_incercate:
        total.append(cuvant)
    numar_incercari_ramase = 6 - numar_incercari
    for rest in range(numar_incercari_ramase):
        total.append(" ".join(["_"] * 5))
    interfata(total)

def citire_dictionar():
    fisier_dictionar = open("cuvinte_wordle.txt",'r')
    continut = fisier_dictionar.read()
    global dictionar
    dictionar = continut.split()
    fisier_dictionar.close()

def cuvantul_are_5_litere(cuvant):
    if(len(cuvant) != 5):
        print("Cuvantul introdus nu are 5 litere.")
        print("Te rog incearca din nou",sep = "\n")
        cuvant = input().upper()
        os.system('cls')
    return cuvant

def cuvantul_este_in_dictionar(cuvant):
    if(cuvant not in dictionar):
        print("Cuvantul nu exista in lista de cuvinte")
        print("Incearca din nou!")
        cuvant = input().upper()
        os.system('cls')
    return cuvant

def citire_cuvant():
    cuvant = input("Incercarea ta este: ").upper()
    print()
    return cuvant

def wordle():
    citire_dictionar()
    global numar_incercari
    raspuns_corect = random.choice(dictionar)
    cuvantul_este_ghicit = False
    while cuvantul_este_ghicit != True and numar_incercari < 6:
        cuvant_incercat = citire_cuvant()
        os.system('cls')
        if(cuvant_incercat == "QUIT"):
            return
        cuvant_incercat = cuvantul_are_5_litere(cuvant_incercat)
        cuvant_incercat = cuvantul_este_in_dictionar(cuvant_incercat)
        numar_incercari += 1
        cuvantul_este_ghicit = ghicire(raspuns_corect,cuvant_incercat)
        afisare(cuvinte_incercate)
    if cuvantul_este_ghicit == True:
        print(f"Bravo! Ai ghicit cuvantul din {numar_incercari} incercari")
    else:
        print(f"Ai pierdut! Cuvantul era {raspuns_corect}")

wordle()