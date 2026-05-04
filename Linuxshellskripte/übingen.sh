#!/bin/bash

# Datei prüfen
DATEI="test.txt"

if [ -f "$DATEI" ]; then
    echo "Datei existiert"
else
    echo "Datei existiert nicht, wird erstellt"
    touch "$DATEI"
fi

# Inhalt hinzufügen
echo -e "Apfel\nBanane\nKirsche\nApfel" > $DATEI

# Stringlänge
TEXT="Hallo Welt"
echo "Länge von '$TEXT': ${#TEXT}"

# cut (erste Spalte)
echo "Max;Mustermann;20" | cut -d ";" -f1

# sort + uniq
echo "Sortiert & ohne Duplikate:"
sort $DATEI | uniq

# grep
echo "Suche nach 'Apfel':"
grep "Apfel" $DATEI

# Array mischen (shuffle)
ARRAY=(1 2 3 4 5)
echo "Gemischtes Array:"
printf "%s\n" "${ARRAY[@]}" | shuf

# Pipe Beispiel
cat $DATEI | grep "Apfel" | sort

# Backup mit tar
mkdir -p backup
tar -cvf backup/backup.tar $DATEI
echo "Backup erstellt!"
