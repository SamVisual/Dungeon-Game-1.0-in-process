from art import *
from colorama import Fore, Back, Style
from .menu import menue_wil

def welc():
 print("\n\n\n\n")
 tprint(f"            Wilkommen  im\n----Dungeon----")



def name():
    name = input("Wähle deinen Namen, Reisender: ")
    print(f"Hallo {name}, Wilkommen im Dungeon")
    print("\n\nDu bist jetzt im Dungeon gefangen und musst einen ausweg Suchen.\nIm Reiter (Aufgaben), findest du deine Tasks.")
    print("\n\n\n")
    menue_wil()
