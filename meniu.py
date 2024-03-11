from os import system
from termcolor import cprint

def meniu():

    cprint("---JOC WORDLE---", "grey","on_red",attrs=["bold", "underline"])
    cprint("1.JOCUL DE WORDLE OBISNUIT","white","on_red",attrs=["underline"])
    cprint("2.BOTUL DE WORDLE","white","on_red",attrs=["underline"])
    cprint("IESI DIN JOCUL DE WORDLE(orice tasta)","white","on_red",attrs=["underline"])

meniu()
alegere=int(input())

while alegere!=0:
    if alegere == 1:
        system('cls')
        from game_console import wordle
        wordle()
    elif alegere == 2:
        system('cls')
        from bot import wordle_bot
        wordle_bot()
    else:
        system('cls')
        print("La revedere!")
        break