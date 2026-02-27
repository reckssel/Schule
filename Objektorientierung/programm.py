from mensch import Mensch

ich = Mensch()
otto = Mensch()

ich.set_Vorname("Emil")
ich.set_nachname("Zin")
ich.set_alter("19")

otto.set_Vorname("Otto")
otto.set_nachname("Franz")
otto.set_alter("234")

print(ich.get_Vorname() + " " + ich.get_nachname() + " ist " + ich.get_alter() +  " Jahre alt " + ich.get_Famienstand())
print(otto.get_Vorname() + " " + otto.get_nachname() + " ist " + otto.get_alter() +  " Jahre alt " + otto.get_Famienstand())