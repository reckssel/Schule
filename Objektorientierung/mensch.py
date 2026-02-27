class Mensch:
    __vorname = str("")
    __nachname = str("")
    __alt = int()
    __familienstand = str("")

    def get_alter(self):
        return self.__alt
    def set_alter(self, value):
        self.__alt=int(value)
    
    def geburtstag(self):
        self.__alt += 1

    def get_Vorname(self):
        return self.__vorname
    def set_Vorname(self, value):
        self.__vorname=value
    
    def get_nachname(self):
        return self.__nachname
    def set_nachname(self, value):
        self.__nachname=value
    
    def get_Familienstand(self):
        return self.__familienstand
    def set_Familienstand(self, value):
        self.__familienstand=value
    def heiraten(self):
        self.__familienstand = "verheiratet"
        self.set_nachname(self.__nachname + "-Müller")
    # -------------------------
    # Constructor
    # -------------------------
    def __init__(self):
        self.__vorname = ""
        self.__nachname = ""
        self.__alt = 0
        self.__familienstand = "ledig"
