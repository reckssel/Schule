try:
    inhalt = open("alphabet.txt")
    
    zeichen = "s"
    while zeichen !="":
        zeichen=inhalt.read(1)
        print(zeichen, "-->", ord(zeichen), ":", chr(ord(zeichen)-32), "-->", ord(chr(ord(zeichen)-32)))
except FileNotFoundError:
    print("❌ Datei Wurde nicht gefunden")