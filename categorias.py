import sqlite3

conn = sqlite3.connect("ventas.db")
cursor = conn.cursor()

categorias = [("Electrónica",), ("Accesorios",), ("Software",)]
cursor.executemany("INSERT INTO Categorias (Nombre) VALUES (?)", categorias)

conn.commit()
conn.close()
