import sqlite3
con = sqlite3.connect('arqui.db')
cur = con.cursor()
cur.execute("SELECT * FROM usuariomascota")
print(cur.fetchall())
con.close()
