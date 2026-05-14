


import sqlite3
import csv
import pandas as pd


conn = sqlite3.connect('persona5_skills.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS p5r_skills (
    element TEXT NOT NULL,           -- Physical, Fire, Ice, Electric, Wind, Psychic, Nuclear, Bless, Curse, Almighty, Gun, Healing, Support, Ailment, Passive, Other
    skill_name TEXT NOT NULL UNIQUE,
    effect TEXT,
    power INTEGER,                   -- Base power (NULL for non-damage skills)
    accuracy REAL,                   -- e.g., 0.90 for 90%
    crit_rate REAL,                  -- e.g., 0.20 for 20%
    ailment_chance REAL,             -- e.g., 0.35 for 35%
    cost TEXT,                       -- e.g., "5% HP", "4 SP", "N/A"
    notes TEXT                     -- Unique, DLC, how to obtain, etc.
);''')


print("Persona 5: Royal Skill Table created.")

data = []

with open("persona5_skills.csv",mode="r",newline="",encoding="utf-8") as file:
    reader = csv.reader(file)

    #Skipping header
    next(reader)

    for row in reader:
        data.append(tuple(row))


cursor.executemany('''INSERT OR REPLACE INTO p5r_skills (element, skill_name, effect, power, accuracy, crit_rate, ailment_chance, cost, notes)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)


conn.commit()
print("Skills from wiki loaded successfully.")
conn.close()


