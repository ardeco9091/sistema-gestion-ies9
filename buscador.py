import pandas as pd

def buscar_alumno(termino):
    try:
        # Cargar los datos
        df = pd.read_csv('alumnos.csv')
        
        # Convertir el término de búsqueda a texto limpio
        busqueda = str(termino).strip()
        
        # ESTRATEGIA DE BÚSQUEDA EN CASCADA
        
        # 1. Intentar buscar por DNI (Coincidencia Exacta)
        # Convertimos la columna DNI a string para comparar texto con texto
        resultado = df[df['dni'].astype(str) == busqueda]
        
        # 2. Si no hay resultados, buscar por EMAIL (Que contenga el texto)
        if resultado.empty:
            # case=False ignora mayúsculas/minúsculas
            resultado = df[df['email'].str.contains(busqueda, case=False, na=False)]
            
        # 3. Si sigue vacío, buscar por NOMBRE (Que contenga el texto)
        if resultado.empty:
            resultado = df[df['nombre'].str.contains(busqueda, case=False, na=False)]
            
        # RETORNO DE RESULTADOS
        if not resultado.empty:
            # Devuelve el PRIMER alumno que coincida (fila 0) convertido a diccionario
            return resultado.iloc[0].to_dict()
        else:
            return None
            
    except Exception as e:
        print(f"Error en buscador: {e}")
        return None
