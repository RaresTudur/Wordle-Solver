import string
from termcolor import colored
fisier_dictionar = open("cuvinte_wordle.txt",'r')
fisier_solutie = open("solutie.txt",'w')
#citirea dictionarului
continut = fisier_dictionar.read()
dictionar = continut.split()
fisier_dictionar.close()
for i in range(len(dictionar)):
    dictionar[i]= dictionar[i].lower()


def literecorecte(rezultat,cuvant_incercat):
    litere_corecte = []
    for i in range(5):
        if rezultat[i] == "C" :
            litere_corecte.append([cuvant_incercat[i],i])
    return litere_corecte

def litereposibile(rezultat,cuvant_incercat):
    litere_posibile = []
    for i in range(5):
        if rezultat[i] == "P":
            litere_posibile.append([cuvant_incercat[i],i])
    return litere_posibile

def literegresite(rezultat,cuvant_incercat):
    litere_gresite =[]
    for i in range(5):
        if rezultat[i] == "G":
            litere_gresite.append(cuvant_incercat[i])
    return litere_gresite

def selectare_cuvinte(rezultat,cuvant_incercat,dictionar):
    litere_corecte = literecorecte(rezultat,cuvant_incercat)
    litere_posibile = litereposibile(rezultat,cuvant_incercat)
    litere_gresite = literegresite(rezultat,cuvant_incercat)
    cuvinte_salvatoare_first = []
    cuvinte_salvatoare_second = []
    cuvinte_salvatoare_mid = []
    cuvinte_salvatoare_prefinal = []
    cuvinte_salvatoare_final = []
    litere_folositoare = []
    for c in litere_corecte:
        litere_folositoare.append(c[0])
    for p in litere_posibile:
        litere_folositoare.append(p[0])

    for cuv in dictionar:
        folosibil = True
        for g in litere_gresite:
            if g in cuv:
                if g in litere_folositoare:
                    pass
                else:
                    folosibil = False
                    break
        if folosibil == True:
            cuvinte_salvatoare_first.append(cuv)
    #subtiez lista de cuvinte posibile din ce in ce mai mult
    for cuv in cuvinte_salvatoare_first:
        folosibil = True
        for c in litere_corecte:
            if cuv[c[1]] != c[0]:
                folosibil = False
                break
        if folosibil == True:
            cuvinte_salvatoare_second.append(cuv)
    for cuv in cuvinte_salvatoare_second:
        folosibil = True
        for p in litere_posibile:
            if cuv[p[1]] == p[0]:
                folosibil = False
                break
        if folosibil is True:
            cuvinte_salvatoare_mid.append(cuv)
    for cuv in cuvinte_salvatoare_mid:
        folosibil = True
        for c in litere_folositoare:
            if c not in cuv:
                folosibil = False
                break
        if folosibil == True:
            cuvinte_salvatoare_prefinal.append(cuv)
    for cuv in cuvinte_salvatoare_prefinal:
        folosibil = True
        for g in litere_gresite:
            if g in litere_folositoare:
                if cuv.count(g) != litere_folositoare.count(g):
                    folosibil = False
                    break
        if folosibil == True:
            cuvinte_salvatoare_final.append(cuv)
    return cuvinte_salvatoare_final

def frecventa_literelor(dictionar):
    alfabet = string.ascii_lowercase
    frecvental ={}
    for l in alfabet:
        fr = [0,0,0,0,0]
        for i in range(5):
            for cuv in dictionar:
                if cuv[i] == l:
                    fr[i] += 1
        frecvental.update({l:fr})
    return frecvental

def posibilitatecuvant(dictionar,frecventa):
    cuvinte = {}
    frecventa_maxima = [0,0,0,0,0]
    for i in frecventa:
        for j in range(5):
            if frecventa_maxima[j] < frecventa[i][j]:
                frecventa_maxima[j] = frecventa[i][j]
    for cuv in dictionar:
        posiblitate = 1
        for i in range(5):
            litera = cuv[i]
            posiblitate *= 1 + (frecventa[litera][i] - frecventa_maxima[i]) ** 2
        cuvinte.update({cuv:posiblitate})
    return cuvinte

def cuvantul_posibil(dictionar,frecventa):
    posibilitate_maxima = 10000000000000000000000000000000000000000000000000000000000000000000
    cuvantulposibil = "acasa"
    posibilitate = posibilitatecuvant(dictionar,frecventa)
    for cuv in dictionar:
        if posibilitate[cuv] < posibilitate_maxima:
            posibilitate_maxima = posibilitate[cuv]
            cuvantulposibil = cuv
    return cuvantulposibil

def ghicire(raspuns_corect,cuvant_incercat):
    pozitie = 0
    hint = ""
    for l in cuvant_incercat:
        if l == raspuns_corect[pozitie]:
            hint += "C"
        elif l in raspuns_corect:
            hint += "P"
        else:
            hint += "G"
        pozitie += 1
    return hint

def wordle_bot(dictionar,cuvant):
    #botul recomanda din prima un cuvant ca sa minimalizeze numarul de incercari
    cuvant_recomandat = "tarei"
    numar_incercari = 1
    rezultat = ghicire(cuvant,cuvant_recomandat)
    print(rezultat)
    while rezultat != "CCCCC":
        dictionar = selectare_cuvinte(rezultat,cuvant_recomandat,dictionar)
        if(len(dictionar) == 0):
            print("Nu am reusit")
            break
        cuvant_recomandat = cuvantul_posibil(dictionar,frecventa_literelor(dictionar))
        fisier_solutie.write(f"{cuvant_recomandat.upper()} ")
        rezultat = ghicire(cuvant,cuvant_recomandat)
        numar_incercari += 1
    if(rezultat == "CCCCC"):
        print(f"Am rezolvat wordle in {numar_incercari} incercari")
    fisier_solutie.write("\n")
    fisier_solutie.write(f"Cuvantul cautat este {cuvant.upper()} si a fost gasit in {numar_incercari} incercari")
    fisier_solutie.write("\n")
    return numar_incercari


def verificare_bot():
    sum_medie = 0
    for cuvant in dictionar:
        sum_medie += wordle_bot(dictionar,cuvant)
    print(sum_medie)
    fisier_solutie.close()

verificare_bot()

