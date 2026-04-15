import random
import sqlite3

conn = sqlite3.connect("spiel.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS spieler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    versuche INTEGER NOT NULL
)""")

conn.commit()
conn.close()

def save_score(name, versuche):
    conn = sqlite3.connect("spiel.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO spieler (name, versuche) VALUES (?, ?)', (name, versuche))
    conn.commit()
    conn.close()

def show_leaderboard():
    conn = sqlite3.connect("spiel.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name, versuche FROM spieler ORDER BY versuche ASC')
    scores = cursor.fetchall()
    print("\n🏆 Bestenliste 🏆")
    for idx, (name, versuche) in enumerate(scores, start=1):
        print(f"{idx}. {name} - {versuche} Versuche")
    conn.close()

def zahlenratespiel():
    print("🎯 Willkommen zum Zahlenratespiel!")
    print("Ich denke mir eine Zahl zwischen 1 und 100...")

    geheimzahl = random.randint(1, 100)
    versuche = 0

    while True:
        try:
            tipp = int(input("Dein Tipp: "))
            versuche += 1

            if tipp < geheimzahl:
                print("Zu niedrig! 📉")
            elif tipp > geheimzahl:
                print("Zu hoch! 📈")
            else:
                print(f"🎉 Richtig! Die Zahl war {geheimzahl}.")
                print(f"Du hast {versuche} Versuche gebraucht.")
                return versuche

        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")

name = input("Bitte geben Sie Ihren Namen ein: ")
print(f"Hallo, {name}! Viel Spaß beim Spielen.")
versuche = zahlenratespiel()
save_score(name, versuche)
show_leaderboard()