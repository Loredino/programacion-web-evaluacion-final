from flask import (
        flash,
        Flask,
        g,
        render_template,
        redirect,
        request,
        session,
        url_for
    )
from flask_wtf.csrf import CSRFProtect, generate_csrf
from pymongo import MongoClient
from werkzeug.exceptions import BadRequestKeyError
import bcrypt

MONGO_URI = "mongodb://localhost:27017/"
BD_NOMBRE = "loredana_romano"
C_USUARIOS = "usuarios"

app = Flask(__name__,
        template_folder='templates',
        static_folder='static'
    )
# Configura protección CSRF para forms
app.config["SECRET_KEY"] = "tcicPXSQJOwCtZFbwFXz"
csrf = CSRFProtect(app)

def get_bd() -> MongoClient:
    '''Obtiene la conexión a mongodb y la setea en g.mongo.'''
    global MONGO_URI
    if "mongo" not in g:
        g.mongo = MongoClient(MONGO_URI)

    return g.mongo


@app.context_processor
def csrf_token():
    return dict(csrf_token=generate_csrf())

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/ejercicio1', methods=("GET", "POST"))
def ejercicio_uno():
    resultados = []

    # Procesar post
    if request.method == "POST":
        try:
            nombre = request.form["nombre"]
            edad = int(request.form["edad"])
            cantidad_tarros = int(request.form["tarros"])

        # Uno de los campos no viene
        except BadRequestKeyError:
            flash("¡Todos los campos son obligatorios!")
            return redirect(url_for("ejercicio_uno"))

        # Error en conversión a int
        except ValueError:
            flash("¡Campos edad y cantidad de tarros deben ser enteros!")
            return redirect(url_for("ejercicio_uno"))

        # Campos inválidos
        if not nombre or not edad or not cantidad_tarros:
            flash("¡Todos los campos son obligatorios!")
            return redirect(url_for("ejercicio_uno"))

        # Edad negativa
        if edad < 0:
            flash("¡La edad debe ser mayor a 0!")
            return redirect(url_for("ejercicio_uno"))

        # Cantidad de tarros negativa
        if cantidad_tarros < 0:
            flash("!La cantidad de tarros debe ser mayor a 0!")
            return redirect(url_for("ejercicio_uno"))

        valor_tarro = 9000
        dcto = 0 # en porciento
        monto_dcto = 0 # monto a descontar
        subtotal = 0 # s/dcto
        total = 0 # c/dcto

        # Calcular descuentos
        if edad >= 18 and edad <= 30:
            dcto = 15
        elif edad > 30:
            dcto =25

        # Calcular total
        subtotal = valor_tarro * cantidad_tarros
        monto_dcto = round(subtotal * (dcto / 100))
        total = round(subtotal - monto_dcto)

        # Resultados
        resultados.append(f"Nombre del cliente: {nombre}")
        resultados.append(f"Total sin descuento: ${subtotal}")
        resultados.append(f"El descuento es: ${monto_dcto}")
        resultados.append(f"El total a pagar es de: ${total}")
        print(resultados)

    return render_template(
            f"ejercicios/1.html",
            resultados=resultados
        )

@app.route('/ejercicio2', methods=("GET", "POST"))
def ejercicio_dos():
    global BD_NOMBRE, C_USUARIOS

    error = "¡Usuario o contraseña incorrectos!"
    usuario_logueado = False
    mensaje_bienvenida = ""
    roles = {
        "juan": "administrador",
        "pepe": "usuario"
    }

    if request.method == "POST":
        try:
            usuario = request.form["nombre"]
            clave = request.form["clave"]
        # No vienen campos
        except BadRequestKeyError:
            flash(error)
            return redirect(url_for("ejercicio_dos"))

        # Conecta con mongo
        bd = get_bd()[BD_NOMBRE]
        usuarios = bd[C_USUARIOS]

        # Verifica que exista el usuario
        r = list(usuarios.find({"nombre": usuario}))

        # Usuario no se encontró
        if not r:
            flash(error)
            return redirect(url_for("ejercicio_dos"))

        # Valida clave
        clave_valida = bcrypt.checkpw(clave.encode(), r[0]["clave"].encode())

        # Clave invalida
        if not clave_valida:
            flash(error)
            return redirect(url_for("ejercicio_dos"))

        # Usuario logueado correctamente
        usuario_logueado = True
        mensaje_bienvenida = f"Bienvenido {roles[usuario]} {usuario}"

    return render_template(
            f"ejercicios/2.html",
            usuario_logueado=usuario_logueado,
            mensaje_bienvenida=mensaje_bienvenida
        )
