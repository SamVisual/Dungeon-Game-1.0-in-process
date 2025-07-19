from Funktionen.CHaa.has import todesanzeige
from art import *

class Charakter:
    def __init__(self, name, leben, staerke):
        self.leben = leben
        self.staerke = staerke

    def ist_tot(self):
        return self.leben <= 0
    
    def __str__(self):
     return f"(❤️ {self.leben}, 💪 {self.staerke})" 
held = Charakter("Held", 0, 20) #Helden Statistiken
def leben():
   if held.leben <= 0:
      todesanzeige()
      tprint("Der Spieler ist Tot")
      


leben()