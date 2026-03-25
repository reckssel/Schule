import sqlite3

conn = sqlite3.connect("tiere.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tiere (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    art TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")

conn.commit()
conn.close()
def add_tier(name, art, age):
    conn = sqlite3.connect("tiere.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tiere (name, art, age) VALUES (?, ?, ?)', (name, art, age))
    conn.commit()
    conn.close()

def get_all_tiere():
    conn = sqlite3.connect("tiere.db")
    cursor = conn.cursor()  
    cursor.execute('SELECT * FROM tiere')
    return cursor.fetchall()
def delete_tier(tier_id):
    conn = sqlite3.connect("tiere.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tiere WHERE id = ?', (tier_id,))
    conn.commit()
    conn.close()

while True:
    print("1. Tier hinzufügen")
    print("2. Alle Tiere anzeigen")
    print("3. Tier löschen")
    print("4. Beenden")
    choice = input("Wählen Sie eine Option: ")
    
    if choice == '1':
        name = input("Name des Tieres: ")
        art = input("Art des Tieres: ")
        alter = int(input("Alter des Tieres: "))
        add_tier(name, art, alter)
        print("Tier hinzugefügt!")
        
    elif choice == '2':
        tiere = get_all_tiere()
        for tier in tiere:
            print(f"ID: {tier[0]}, Name: {tier[1]}, Art: {tier[2]}, Alter: {tier[3]}")
            
    elif choice == '3':
        tier_id = int(input("ID des zu löschenden Tieres: "))
        delete_tier(tier_id)
        print("Tier gelöscht!")
        
    elif choice == '4':
        break
    else:
        print("Ungültige Option, bitte erneut versuchen.")
