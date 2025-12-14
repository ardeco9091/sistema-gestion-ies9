from flask import Flask, render_template, request
import os
import traceback # Esta librería sirve para "rastrear" el error

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        # Si falla, te mostrará el error en la web
        return f"<h1>Error al cargar inicio:</h1><pre>{traceback.format_exc()}</pre>"

@app.route('/resultado', methods=['POST'])
def resultado():
    try:
        # Importamos aquí adentro para ver si el error está en buscador.py
        from buscador import buscar_alumno
        
        dni = request.form.get('dni')
        if not dni:
            return "No ingresaste DNI"
            
        alumno = buscar_alumno(dni)
        
        if alumno:
            return render_template('resultado.html', alumno=alumno)
        else:
            return "Alumno no encontrado (Revisa el CSV)"
            
    except Exception as e:
        # ¡AQUÍ ESTÁ LA CLAVE! 
        # Esto imprimirá el error real en tu pantalla
        return f"<h1>Ocurrió un error en el sistema:</h1><pre>{traceback.format_exc()}</pre>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
