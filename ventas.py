import sqlite3
from datetime import datetime

conn = sqlite3.connect("ventas_db.sql")
cursor = conn.cursor()

ventas = [
    (1, 1, datetime.now().isoformat(), 2),
    (2, 2, datetime.now().isoformat(), 1)
]

cursor.executemany("INSERT INTO Ventas (ClienteID, ProductoID, Fecha, Cantidad) VALUES (?, ?, ?, ?)", ventas)
conn.commit()
conn.close()
