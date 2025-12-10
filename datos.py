# archivo: datos.py
import csv
import os

def cargar_base_de_datos():
    """
    Carga los alumnos desde el archivo CSV.
    Si no existe, devuelve una lista vacía.
    """
    lista_alumnos = []
    nombre_archivo = 'alumnos.csv'
    
    # Ruta absoluta para asegurar que encuentre el archivo en cualquier sistema
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_base, nombre_archivo)

    try:
        with open(ruta_completa, mode='r', encoding='utf-8') as archivo:
            # DictReader convierte cada linea del CSV en un Diccionario automáticamente
            lector = csv.DictReader(archivo)
            for fila in lector:
                lista_alumnos.append(fila)
        print(f"✅ Base de datos cargada: {len(lista_alumnos)} alumnos encontrados.")
    except FileNotFoundError:
        print(f"⚠️ Error: No se encontró el archivo {nombre_archivo}. Usando lista vacía.")
    
    return lista_alumnos

# Esta variable se usará en app.py y buscador.py
BD_ALUMNOS = cargar_base_de_datos()