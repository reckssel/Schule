class Fahrer:
    def __init__(self, name, alter, führerschein):
        self.name = name
        self.alter = alter
        self.führerschein = führerschein
    
    def geburtstag_feiern(self):
        self.alter += 1
        print(f"{self.name} feiert seinen Geburtstag! Er ist jetzt {self.alter}.")

class Straßenbahn:
    def __init__(self, bahnname, passagierzahl, stammlinie, fahrer):
        self.bahnname = bahnname
        self.passagierzahl = passagierzahl
        self.stammlinie = stammlinie
        self.fahrer = fahrer
    def change_stammlinie(self, neue_stammlinie):
        self.stammlinie = neue_stammlinie
        print(f"{self.bahnname} wechselt zur Stammlinie {self.stammlinie}.")
    
Fahrer1 = Fahrer("Max", 30, True)
Straßenbahn1 = Straßenbahn("Tram 1", 100, "Linie A", Fahrer1)
print(f"{Straßenbahn1.bahnname} hat {Straßenbahn1.passagierzahl} Passagiere und fährt auf {Straßenbahn1.stammlinie}. Der Fahrer ist {Straßenbahn1.fahrer.name}.")
Straßenbahn1.change_stammlinie("Linie B")
Fahrer1.geburtstag_feiern()
print(f"{Straßenbahn1.bahnname} hat jetzt {Straßenbahn1.passagierzahl} Passagiere und fährt auf {Straßenbahn1.stammlinie}. Der Fahrer ist {Straßenbahn1.fahrer.name} und ist jetzt {Straßenbahn1.fahrer.alter} Jahre alt.")
    