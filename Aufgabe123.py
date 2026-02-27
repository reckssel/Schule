MAX_GRUPPEN = 130
PERSONEN_PRO_GRUPPE = 4

gruppen = []          # mehrdimensionale Liste
aktuelle_gruppe = []

try:
    with open("Namen-+.txt", "r", encoding="utf-8") as datei:
        for zeile in datei:
            name = zeile.strip()

            if not name:
                continue  # leere Zeilen überspringen

            aktuelle_gruppe.append(name)

            # Gruppe ist voll
            if len(aktuelle_gruppe) == PERSONEN_PRO_GRUPPE:
                if len(gruppen) < MAX_GRUPPEN:
                    gruppen.append(aktuelle_gruppe)
                aktuelle_gruppe = []

            # Maximale Gruppenzahl erreicht
            if len(gruppen) == MAX_GRUPPEN:
                break

        # letzte (unvollständige) Gruppe hinzufügen
        if aktuelle_gruppe and len(gruppen) < MAX_GRUPPEN:
            gruppen.append(aktuelle_gruppe)

except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")
except IOError:
    print("Fehler beim Lesen der Datei.")

# Ausgabe
print(f"Benötigte Gruppen: {len(gruppen)}")

for i, gruppe in enumerate(gruppen, start=1):
    print(f"Gruppe {i}: {gruppe}")
