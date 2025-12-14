from flask import Flask, render_template, request, redirect, url_for
from buscador import buscar_alumno
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    # Recibimos el DNI del formulario
    dni_ingresado = request.form.get('dni')
    
    # Validación básica
    if not dni_ingresado:
        # Si está vacío, volvemos al inicio sin mostrar errores feos
        return redirect(url_for('index'))
    
    # Buscamos usando tu lógica de Pandas
    alumno_encontrado = buscar_alumno(dni_ingresado)
    
    if alumno_encontrado:
        # ¡ÉXITO! Mostramos el Dashboard profesional
        return render_template('resultado.html', alumno=alumno_encontrado)
    else:
        # Si no existe, podríamos mostrar un error, 
        # pero por ahora volvemos al index para que sea limpio.
        return render_template('index.html', error="Alumno no encontrado")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
