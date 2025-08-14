import os
import sys

def mostrar_menu():
    print("\n📊 MENÚ PRINCIPAL - PROYECTO VENTAS")
    print("1. Ejecutar mantenedor")
    print("2. Leer CSV y mostrar datos")
    print("3. Exportar ventas a Excel")
    print("4. Ejecutar dashboard")
    print("5. Salir")

def ejecutar_mantenedor():
    os.system("python mantenedor/mantenedor.py")

def leer_csv():
    from leer_y_exportar import lectura
    print("\nArchivos disponibles:")
    print("1. clientes.csv")
    print("2. productos.csv")
    print("3. ventas.csv")
    opcion = input("Selecciona archivo a leer: ")
    archivo = {
        "1": "datos/clientes.csv",
        "2": "datos/productos.csv",
        "3": "datos/ventas.csv"
    }.get(opcion)
    if archivo:
        lectura.leer_csv(archivo)
    else:
        print("❌ Opción inválida.")

def exportar_excel():
    from reportes import exportar_excel
    exportar_excel.exportar_ventas_excel()

def ejecutar_dashboard():
    os.system("streamlit run dashboard/dashboard.py")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        if opcion == "1":
            ejecutar_mantenedor()
        elif opcion == "2":
            leer_csv()
        elif opcion == "3":
            exportar_excel()
        elif opcion == "4":
            ejecutar_dashboard()
        elif opcion == "5":
            print("👋 Cerrando el sistema.")
            sys.exit()
        else:
            print("⚠️ Opción no válida.")
