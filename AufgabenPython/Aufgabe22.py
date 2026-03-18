# BMI Rechner

gewicht = float(input("Gewicht in kg: "))
groesse = float(input("Größe in Metern (z.B. 1.75): "))

bmi = gewicht / (groesse * 2)

print(f"Dein BMI beträgt: {bmi:.2f}")

if bmi < 18.5:
    print("Kategorie: Untergewicht")
elif bmi < 25:
    print("Kategorie: Normalgewicht")
elif bmi < 30:
    print("Kategorie: Übergewicht")
else:
    print("Kategorie: Adipositas")
