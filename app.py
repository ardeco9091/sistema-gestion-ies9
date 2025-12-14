from flask import Flask, render_template, request, redirect, url_for
from buscador import buscar_alumno
import os

app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = 'tu_clave_secreta_super_segura'

@app.route('/')
def index():
    # Renderiza la portada de búsqueda
    return render_template('index.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    dni = request.form.get('dni')
    
    if not dni:
        return redirect(url_for('index'))
    
    # Usamos la nueva función inteligente con Pandas
    alumno_encontrado = buscar_alumno(dni)
    
    if alumno_encontrado:
        # Si existe, mostramos el Dashboard
        return render_template('resultado.html', alumno=alumno_encontrado)
    else:
        # Si no existe, volvemos al inicio con un mensaje de error
        # Nota: Para ver el mensaje necesitas configurar mensajes flash en el html, 
        # pero por ahora simplemente recargará.
        return render_template('index.html', error="Alumno no encontrado")

# Esta parte es vital para que Render arranque la app
if __name__ == '__main__':
    # Obtiene el puerto del entorno de Render o usa 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
