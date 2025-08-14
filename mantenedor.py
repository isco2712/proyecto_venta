import sqlite3
import pandas as pd

def agregar_cliente(nombre, email):
    conn = sqlite3.connect("ventas_db.sql")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (Nombre, Email) VALUES (?, ?)", (nombre, email))
    conn.commit()
    conn.close()

def listar_clientes():
    conn = sqlite3.connect("ventas_db.sql")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Clientes")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def eliminar_cliente(cliente_id):
    conn = sqlite3.connect("ventas_db.sql")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Clientes WHERE ClienteID = ?", (cliente_id,))
    conn.commit()
    conn.close()

def agregar_cliente(nombre, email, region_id):
    conn = sqlite3.connect("ventas_db.sql")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Clientes (Nombre, Email, RegionID) VALUES (?, ?, ?)", (nombre, email, region_id))
    conn.commit()
    conn.close()

def listar_ventas_detalladas():
    conn = sqlite3.connect("ventas_db.sql")
    cursor = conn.cursor()
    query = """
    SELECT v.VentaID, c.Nombre, p.Nombre, v.Fecha, v.Cantidad, p.Precio,
           (v.Cantidad * p.Precio) AS Total
    FROM Ventas v
    JOIN Clientes c ON v.ClienteID = c.ClienteID
    JOIN Productos p ON v.ProductoID = p.ProductoID
    """
    for row in cursor.execute(query):
        print(row)
    conn.close()

def insertar_clientes_manualmente():
    conn = sqlite3.connect("ventas_db.sql")
    cursor = conn.cursor()
    clientes = [
        ("Francisco", "fco@email.com"),
        ("Alicia", "fco@email.com")
    ]
    cursor.executemany("INSERT INTO Clientes (Nombre, Email) VALUES (?, ?)", clientes)
    conn.commit()
    conn.close()

def insertar_clientes_desde_csv():
    df = pd.read_csv("clientes.csv")
    conn = sqlite3.connect("ventas_db.sql")
    df.to_sql("Clientes", conn, if_exists="append", index=False)
    conn.close()

if __name__ == "__main__":
    insertar_clientes_manualmente()
    insertar_clientes_desde_csv()
