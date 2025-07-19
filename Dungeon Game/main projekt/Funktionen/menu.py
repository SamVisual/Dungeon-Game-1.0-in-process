import sys
from colorama import Fore, Back, Style

def setting():
   print("------------------------------------------")
   while True: 
    eingabe = input(f"{Fore.RED}(q)Beenden{Style.RESET_ALL} - (w)Zurück\nEingabe: ")
    if eingabe == "q":
       eingabe2 = input(f"\n\n\n\n\n\nSicher das du das Programm Beende willst? {Fore.RED}(Ja/Nein){Style.RESET_ALL}\nEingabe: ")
       if eingabe2 == "Ja":
        sys.exit()
       elif eingabe2 == "Nein":
          print("------------------------------------------")
          continue
       else:
          print(f"{Fore.RED}\n\n\nFehler bei der Eingabe!\nVersuche es erneut.\n\n{Style.RESET_ALL}")
          print("------------------------------------------")
          continue
    elif eingabe == "w":
       print("------------------------------------------")
       print("\n\n\n")
       menue_wil()
    else:
       print(f"\n\n\n{Fore.RED}Fehler bei der Eingabe!\nVersuche es erneut.{Style.RESET_ALL}\n\n\n\n")
       print("------------------------------------------")
       continue

def menue_wil():
    print("\n\n\n\n\n------------------------------------------")
    while True:
        eingabe = input("(q)Menü - (w)Starten\nEingabe: ")
        if eingabe == "q":
            print("\n\n\n\n\n\n")
            setting()
        elif eingabe == "w":
            print("\n\n\n\n\n\n")
            break

        else:    
            print(f"\n\n\n\n\n{Fore.RED}Fehler bei der Eingabe!\nVersuche es erneut.{Style.RESET_ALL}\n\n\n\n")
            print("------------------------------------------")
            continue
