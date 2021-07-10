import sqlite3

conn = sqlite3.connect('arqui.db')  # You can create a new database by changing the name within the quotes
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE mascota
             (idmascota INTEGER PRIMARY KEY,nombre varchar(50), edad integer, raza varchar(50), descripcion varchar(264))''')

# Create table - COUNTRY
c.execute('''CREATE TABLE usuariomascota
             (idrelmp INTEGER PRIMARY KEY,idmascota integer, idusuario integer)''')

# Create table - DAILY_STATUS
c.execute('''CREATE TABLE usuario
             (idusuario INTEGER PRIMARY KEY AUTOINCREMENT, email varchar(50) UNIQUE, nombre varchar(50), apellido varchar(50), rut varchar(50), pass varchar(50), contacto varchar(50), region varchar(50), tipousuario boolean)''')

conn.commit()
