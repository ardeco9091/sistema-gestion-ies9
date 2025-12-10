# -*- coding: utf-8 -*-
def es_email_de_alumno_valido(email):
    if not isinstance(email, str):
        return False
    email_limpio = email.strip().lower()
    dominio_esperado = "@ies9-juj.infd.edu.ar"
    return email_limpio.endswith(dominio_esperado)
