import sqlite3

conn = sqlite3.connect("ventas_db.sql")
cursor = conn.cursor()

productos = [
    ("Laptop", 1200.00),
    ("Mouse", 25.50)
]

cursor.executemany("INSERT INTO Productos (Nombre, Precio) VALUES (?, ?)", productos)
conn.commit()
conn.close()
