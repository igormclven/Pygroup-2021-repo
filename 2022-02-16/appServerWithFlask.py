from flask import Flask

# cuando no se especifica una peticion se ejecuta el get automaticmente

appServerWithFlask = Flask(__name__)

# decorador que muestra
@appServerWithFlask.route("/")
def funcionDeInicio():
    return "<h1>Hola mama, estoy en internet!</h1>"

# en la ruta va a tener un parametro que tomaremos. ESTAS PETICIONES VA A SER GET PORQUE NO LE DECIMOS LO CONTRARIO
@appServerWithFlask.route("/saludo/<string:nombre>")
def funcion(nombre):
    return f"Hola {nombre}"

@appServerWithFlask.route("/calculadora/<int:n1>/<int:n2>/<string:tipo>")
def calculadora(n1,n2,tipo):
    if tipo== "suma":
        return str(n1+n2)

    elif tipo == "resta":
        return str(n1 - n2)

    elif tipo == "multiplicacion":
        return str(n1 * n2)


if __name__ == '__main__':
    appServerWithFlask.run(port=81)
