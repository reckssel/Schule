class Ware:
    __namen = str("")
    __preis = float()
    __bestand = int()
    __bestandpreis = float(__bestand * __preis)

    def get_namen(self):
        return self.__namen
    def set_namen(self, value):
        self.__namen=value
    def get_preis(self):
        return self.__preis
    def set_preis(self, value):
        self.__preis=float(value)
    def get_bestand(self):
        return self.__bestand
    def set_bestand(self, value):
        self.__bestand=int(value)
    def get_bestandpreis(self):
        return self.__bestandpreis
    def entnemen(self, value):
        self.__bestand -= int(value)
    def auffüllen(self, value):
        self.__bestand += int(value)
    # -------------------------
    # Constructor
    # -------------------------
    def __init__(self):
        self.__namen = ""
        self.__preis = 0.0
        self.__bestand = 0
