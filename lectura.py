import pandas as pd
import pdfplumber
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.pagesizes import letter

# Leer CSV
def leer_csv(ruta):
    df = pd.read_csv(ruta)
    print(df.head())
    return df

# Leer texto de PDF
def leer_pdf(ruta):
    texto = ""
    with pdfplumber.open(ruta) as pdf:
        for pagina in pdf.pages:
            texto += pagina.extract_text() + "\n"
    print(texto)
    return texto

# Exportar DF a CSV
def exportar_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False)
    print(f"Archivo CSV exportado: {nombre_archivo}")

# Exportar DataFrame a Excel
def exportar_excel(df, nombre_archivo):
    df.to_excel(nombre_archivo, index=False)
    print(f"Archivo Excel exportado: {nombre_archivo}")

# Exportar DataFrame a PDF
def exportar_pdf(df, nombre_archivo):
    data = [df.columns.tolist()] + df.values.tolist()
    pdf = SimpleDocTemplate(nombre_archivo, pagesize=letter)
    tabla = Table(data)
    pdf.build([tabla])
    print(f"Archivo PDF exportado: {nombre_archivo}")
