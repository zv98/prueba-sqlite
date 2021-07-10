import sqlite3
con = sqlite3.connect('arqui.db')
cur = con.cursor()
cur.execute("INSERT INTO usuariomascota(idusuario,idmascota) VALUES (1,1)")
con.commit()
con.close()
