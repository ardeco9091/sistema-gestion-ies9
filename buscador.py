# -*- coding: utf-8 -*-
def buscar_alumno(termino, lista_alumnos):
    resultados = []
    if not termino or not isinstance(termino, str):
        return []
    termino_normalizado = termino.strip().lower()
    for alumno in lista_alumnos:
        if termino_normalizado in alumno["nombre"].lower() or termino_normalizado == str(alumno["dni"]):
            resultados.append(alumno)
    return resultados
