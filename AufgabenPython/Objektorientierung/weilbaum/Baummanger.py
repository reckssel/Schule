class baum:
    def __init__(self, name, höhe):
        self.__baumname=name
        self.__baumhöhe=höhe
class baummanager:
    def __init__(self):
        self.__baumliste=list()
    def Baumaufnehmen(self, name, höhe):
        neuer_baum = baum(name, höhe)
        self.__baumliste.append(neuer_baum)
    def giesen(self, menge):
        for baum in self.__baumliste:
            print(f"Der Baum {baum._baum__baumname} wird mit {menge} Litern Wasser gegossen.")