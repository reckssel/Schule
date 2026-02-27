class Tier:
    __Name = str("")
    __Art = str("")
    __Hungrig = str("")
    

    def get_name(self):
        return self.__Name
    def set_name(self, value):
        self.__Name=value
    
    def get_art(self):
        return self.__Art
    
    
    def get_hungrig(self):
        return self.__Hungrig
    # -------------------------
    # Your muma
    # -------------------------
    def __init__(self):
        self.__Hungrig=True
        
