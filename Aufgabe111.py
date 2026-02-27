def taschenrechner():
    """Ein einfacher Taschenrechner in Python."""
    print("Willkommen beim Python Taschenrechner")
    print("Wählen Sie eine Operation:")
    print("1: Addieren (+)")
    print("2: Subtrahieren (-)")
    print("3: Multiplizieren (*)")
    print("4: Dividieren (/)")
    print("5: Beenden")

    while True:
     
        wahl = input("Geben Sie die Nummer der Wahl ein (1/2/3/4/5): ")

     
        if wahl == '5':
            print("Taschenrechner wird beendet.")
            break

       
        if wahl in ('1', '2', '3', '4'):
            try:
    
                num1 = float(input("Geben Sie die erste Zahl ein: "))
                num2 = float(input("Geben Sie die zweite Zahl ein: "))
            except ValueError:
                print("Ungültige Eingabe. Bitte geben Sie Zahlen ein.")
                continue

            if wahl == '1':
                ergebnis = num1 + num2
                print(f"Ergebnis: {num1} + {num2} = {ergebnis}\n")

            elif wahl == '2':
                ergebnis = num1 - num2
                print(f"Ergebnis: {num1} - {num2} = {ergebnis}\n")

            elif wahl == '3':
                ergebnis = num1 * num2
                print(f"Ergebnis: {num1} * {num2} = {ergebnis}\n")

            elif wahl == '4':
                if num2 == 0:
                    print("Fehler: Division durch Null ist nicht erlaubt.\n")
                else:
                    ergebnis = num1 / num2
                    print(f"Ergebnis: {num1} / {num2} = {ergebnis}\n")
        else:
            print("Ungültige Eingabe. Bitte wählen Sie eine gültige Option (1-5).\n")



taschenrechner()