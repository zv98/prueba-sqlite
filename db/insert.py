import sqlite3
con = sqlite3.connect('arqui.db')
cursor.execute("INSERT INTO usuariomascota VALUES (1,1)")
con.commit()
con.close()
