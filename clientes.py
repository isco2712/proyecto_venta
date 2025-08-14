import sqlite3
import pandas as pd

conn = sqlite3.connect("ventas.db")
cursor = conn.cursor()

clientes = [
    ("Francisco", "fco@email.com"),
    ("Alicia", "fco@email.com")
]

cursor.executemany("INSERT INTO Clientes (Nombre, Email) VALUES (?, ?)", clientes)
conn.commit()
conn.close()


df = pd.read_csv("clientes.csv")
conn = sqlite3.connect("ventas.db")
df.to_sql("Clientes", conn, if_exists="append", index=False)
conn.close()
