class Lebensmittel:
    __name=str("")
    __vegetarisch=None
    __vegan=None
    __fettgehalt=int()
    __zuckergehalt=int()

    def get_name(self):
        return self.__name
    def set_name(self, value):
        self.__name=value
    
    def get_vegetarisch(self):
        return self.__vegetarisch
    def set_vegetarisch(self, value):
        self.__vegetarisch=value
    
    def get_vegan(self):
        return self.__vegan
    def set_vegan(self, value):
        self.__vegan=value
    
    def get_fettgehalt(self):
        return self.__fettgehalt
    def set_fettgehalt(self, value):
        self.__fettgehalt=value

    def get_zuckergehlt(self):
        return self.__zuckergehalt
    def set_zuckergehlt(self, value):
        self.__zuckergehalt=value
    # -------------------------