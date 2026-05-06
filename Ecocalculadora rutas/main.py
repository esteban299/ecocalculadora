from flask import Flask, render_template, request

app = Flask(__name__)

# ── Función auxiliar ──────────────────────────────────────────────────────────
def result_calculate(size: int, lights: int, devices: int) -> float:
    home_coef    = 100   
    light_coef   = 2.0   
    devices_coef = 5     
    return size * home_coef + lights * light_coef + devices * devices_coef

# ── Rutas de la calculadora ───────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/size/<int:size>')
def select_lights(size):
    return render_template('lights.html', size=size)

@app.route('/size/<int:size>/lights/<int:lights>')
def select_devices(size, lights):
    return render_template('electronics.html', size=size, lights=lights)

@app.route('/size/<int:size>/lights/<int:lights>/devices/<int:devices>')
def show_result(size, lights, devices):
    result = result_calculate(size, lights, devices)
    return render_template('end.html', result=result)

# ── Rutas del formulario ──────────────────────────────────────────────────────
@app.route('/form')
def form():
    return render_template('form.html')

# ────────────────────────────────────────────────────────────────────────────
# TAREA 6 · El backend del formulario (COMPLETA)
# ────────────────────────────────────────────────────────────────────────────
@app.route('/submit', methods=['POST'])
def submit_form():
    # Paso 1 — Leer los campos del formulario
    name    = request.form['name']
    email   = request.form['email']
    address = request.form['address']
    date    = request.form['date']

    # Paso 2 — Guardar en el archivo TXT (Lógica Kodland)
    # Usamos 'a' (append) para que no se borre lo anterior, o 'w' para sobrescribir
    f = open('form.txt', 'a', encoding='utf-8')
    text = f"Nombre: {name}, Email: {email}, Dirección: {address}, Fecha: {date}\n"
    f.write(text)
    f.close()

    # Paso 3 — Leer el archivo para mostrarlo (opcional)
    f = open('form.txt', 'r', encoding='utf-8')
    form_data = f.read()
    f.close()

    # Paso 4 — Enviar los datos a la plantilla
    return render_template(
        'form_result.html',
        name=name,
        email=email,
        address=address,
        date=date,
        form_data=form_data
    )

@app.route('/discard', methods=['POST', 'GET'])
def discard_form_data():
    # Aquí usamos 'w' para vaciar el archivo (Open, Write nada, Close)
    f = open('form.txt', 'w', encoding='utf-8')
    f.write('')
    f.close()

    return render_template(
        'form_result.html',
        name='',
        email='',
        address='',
        date='',
        form_data='',
        message='Datos descartados correctamente.'
    )

if __name__ == '__main__':
    app.run(debug=True)