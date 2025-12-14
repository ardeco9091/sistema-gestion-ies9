from flask import Flask, render_template, request, redirect, url_for
from buscador import buscar_alumno
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    # CAMBIO: Ahora recibimos 'criterio' en lugar de 'dni'
    criterio = request.form.get('criterio')
    
    if not criterio:
        return redirect(url_for('index'))
    
    # La función buscar_alumno ya es inteligente y sabe qué hacer
    alumno_encontrado = buscar_alumno(criterio)
    
    if alumno_encontrado:
        return render_template('resultado.html', alumno=alumno_encontrado)
    else:
        # Pasamos el error para que sepa qué buscaste
        return render_template('index.html', error=f"No encontramos nada con: {criterio}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
