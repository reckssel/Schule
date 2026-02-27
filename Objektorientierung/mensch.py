class Mensch:
    __vorname = str("")
    __nachname = str("")
    __alt = str("")
    __familienstand = str("")

    def get_alter(self):
        return self.__alt
    def set_alter(self, value):
        self.__alt=value
    
    def get_Vorname(self):
        return self.__vorname
    def set_Vorname(self, value):
        self.__vorname=value
    
    def get_nachname(self):
        return self.__nachname
    def set_nachname(self, value):
        self.__nachname=value
    
    def get_Famienstand(self):
        return self.__familienstand
    def set_Familenstand(self, value):
        self.__familienstand=value
    # -------------------------
    # Your muma
    # -------------------------
    def __init__(self):
        self.__familienstand="ledig"
        
