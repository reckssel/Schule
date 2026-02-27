while True:
    dateiname = input("Welches Gedicht möchtest du lesen? (ohne .txt): ").strip()
    dateiname = dateiname + ".txt"

    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            inhalt = datei.read()
            print("\n--- ", dateiname, " ---\n")
            print(inhalt)
            break  # gültige Datei → Schleife beenden

    except FileNotFoundError:
        print("❌ Dieses Gedicht existiert nicht. Bitte erneut eingeben.\n")
    except OSError:
        print("❌ Fehler beim Öffnen der Datei. Bitte erneut versuchen.\n")

