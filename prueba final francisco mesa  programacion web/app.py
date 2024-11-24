from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = int(request.form.get("edad"))
        cantidad = int(request.form.get("cantidad"))
        total_sin_descuento = cantidad * 9000

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_total = total_sin_descuento * descuento
        total_final = total_sin_descuento - descuento_total

        # Crear un diccionario para enviar los resultados
        resultado = {
            "nombre": nombre,
            "total_sin_descuento": total_sin_descuento,
            "descuento": descuento_total,
            "total_final": total_final
        }

        return render_template("ejercicio1.html", resultado=resultado)

    return render_template("ejercicio1.html", resultado=None)


usuarios = {
    "juan": "admin",
    "pepe": "user"
}

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    mensaje = None  # Inicializa el mensaje como None
    if request.method == "POST":
        usuario = request.form.get("usuario")
        password = request.form.get("password")

        # Verificar credenciales
        if usuario in usuarios and usuarios[usuario] == password:
            mensaje = f"¡Bienvenido, {usuario}!"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    # Renderiza la plantilla con el mensaje
    return render_template("ejercicio2.html", mensaje=mensaje)

if __name__ == "__main__":
    app.run(debug=True)