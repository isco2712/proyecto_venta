import streamlit as st
import pandas as pd
import sqlite3
from lectura import exportar_ventas_excel

# Consulta Detalle de ventas
query = """
SELECT
    v.VentaID,
    c.Nombre AS Cliente,
    r.Nombre AS Region,
    p.Nombre AS Producto,
    cat.Nombre AS Categoria,
    v.Fecha,
    v.Cantidad,
    p.Precio,
    (v.Cantidad * p.Precio) AS Total
FROM Ventas v
JOIN Clientes c ON v.ClienteID = c.ClienteID
LEFT JOIN Regiones r ON c.RegionID = r.RegionID
JOIN Productos p ON v.ProductoID = p.ProductoID
LEFT JOIN Categorias cat ON p.CategoriaID = cat.CategoriaID;
"""

# Cargar datos
conn = sqlite3.connect("ventas.db")
df = pd.read_sql_query(query, conn)
conn.close()

# Dashboard
st.title("📊 Dashboard de Ventas")
st.dataframe(df)

# Métrica total
st.metric("💰 Total Ventas", f"${df['Total'].sum():,.2f}")

# Gráfico por región
ventas_por_region = df.groupby("Region")["Total"].sum().reset_index()
st.bar_chart(ventas_por_region.set_index("Region"))

# Exportar a Excel
exportar_ventas_excel()
