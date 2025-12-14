import pandas as pd
import os

def buscar_alumno(dni_buscado):
    archivo_csv = 'alumnos.csv'
    
    if not os.path.exists(archivo_csv):
        return None

    try:
        # Cargamos el CSV con las nuevas columnas de materias
        df = pd.read_csv(archivo_csv, dtype={'dni': str})
        
        # Buscamos al alumno por DNI
        alumno_match = df[df['dni'] == str(dni_buscado)]
        
        if alumno_match.empty:
            return None
        
        datos = alumno_match.iloc[0].to_dict()
        
        # --- MAPEO DE MATERIAS REALES ---
        # Ahora leemos las columnas específicas del nuevo CSV
        # La función float() asegura que sean números para las barras de progreso
        
        def safe_float(val):
            try:
                return float(val)
            except:
                return 0.0

        lista_materias = [
            {'nombre': 'Programación',   'nota': safe_float(datos.get('programacion', 0))},
            {'nombre': 'Base de Datos',  'nota': safe_float(datos.get('base_datos', 0))},
            {'nombre': 'Matemática',     'nota': safe_float(datos.get('matematica', 0))},
            {'nombre': 'Inglés Técnico', 'nota': safe_float(datos.get('ingles', 0))}
        ]

        # Calculamos el promedio real en vivo (más preciso)
        notas_validas = [m['nota'] for m in lista_materias if m['nota'] > 0]
        promedio_calc = round(sum(notas_validas) / len(notas_validas), 1) if notas_validas else 0

        # Objeto final para el Dashboard
        return {
            'nombre': datos.get('nombre', 'Desconocido'),
            'dni': datos.get('dni', ''),
            'carrera': datos.get('carrera', ''),
            'email': datos.get('email', ''),
            'promedio': promedio_calc,  # Usamos el calculado
            'condicion': datos.get('condicion', 'Regular'),
            'materias': lista_materias
        }

    except Exception as e:
        print(f"Error en buscador: {e}")
        return None
