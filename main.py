




import sqlite3

#search test for skill accuracy
skill_name = "Agidyne"

conn = sqlite3.connect('persona5_skills.db')
cursor = conn.cursor()
cursor.execute('''select accuracy from p5r_skills where skill_name = ?''', (skill_name,))

result = cursor.fetchone()

print(result)