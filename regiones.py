import sqlite3

conn = sqlite3.connect("ventas_db.sql")
cursor = conn.cursor()

regiones = [("Metropolitana",), ("Valparaíso",), ("Biobío",)]
cursor.executemany("INSERT INTO Regiones (Nombre) VALUES (?)", regiones)

conn.commit()
conn.close()
