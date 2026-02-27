class PC:
    __speicher = str("")
    __Prozessor = str("")
    __RAM = str("")
    

    def get_speicher(self):
        return self.__speicher
    def set_speicher(self, value):
        self.__speicher=value
    
    def get_prozessor(self):
        return self.__Prozessor
    def set_prozessor(self, value):
        self.__Prozessor=value
    
    def get_ram(self):
        return self.__RAM
    def set_ram(self, value):
        self.__RAM=value

