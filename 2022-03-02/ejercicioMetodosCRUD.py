from flask import Flask, request

# cuando no se especifica una peticion se ejecuta el get automaticmente

appServerWithFlask = Flask(__name__)

estudiantes = []


# Funcion para enviar algo al servidor
@appServerWithFlask.route("/crear", methods=['POST'])
def createStudent():
    # verifica que el metodo que se pide si sea el que estamos programando
    if request.method == 'POST':
        estudiante = dict({"codigo": request.form['cod'], "nombre":request.form['name']})
        estudiantes.append(estudiante)
    return "ok"

# funcion para obtener algo del servidor
@appServerWithFlask.route("/lista", methods=['GET'])
def listStudents():
    # verifica que el metodo que se pide si sea el que estamos programando
    if request.method == 'GET':
        value = ""
        for estudiante in estudiantes:
            value = value + "Nombre: " + estudiante["nombre"] + " Cod: " + estudiante["codigo"] + ".  "
        return value  # une todos los elementos de una dupla en un string

# funcion para editar algo del servidor
@appServerWithFlask.route("/modify/<string:codigo>", methods=['PUT'])
def modifyStudent(codigo):
    if request.method == 'PUT':
    # verifica que el metodo que se pide si sea el que estamos programando
        for estudiante in estudiantes:
            # si codigo está entre los valores que tiene estudiante
            if codigo in estudiante['codigo']:
                estudiante.update(dict({"codigo": request.form['cod'], "nombre":request.form['name']}))
                return "ok" # el return está aqui porque los estudiantes no se pueden espetir, entonces no tiene sentido que siga buscando si lo encuentra
            return "F"

# funcion para eliminar
@appServerWithFlask.route("/delete/<string:codigo>", methods=['DELETE'])
def deleteStudent(codigo):
    # verifica que el metodo que se pide si sea el que estamos programando
    if request.method == 'DELETE':
        for estudiante in estudiantes:
            value = 0
            # si codigo está entre los valores que tiene estudiante
            if codigo in estudiante['codigo']:
                estudiante.remove(value)
                return "ok" # el return está aqui porque los estudiantes no se pueden espetir, entonces no tiene sentido que siga buscando si lo encuentra
            value = value + 1
            return "F"

# decorador que muestra
@appServerWithFlask.route("/")
def funcionDeInicio():
    return "<h1>Hola mama, estoy en internet!</h1>"


# en la ruta va a tener un parametro que tomaremos. ESTAS PETICIONES VA A SER GET PORQUE NO LE DECIMOS LO CONTRARIO
@appServerWithFlask.route("/saludo/<string:nombre>")
def funcion(nombre):
    return f"Hola {nombre}"


@appServerWithFlask.route("/calculadora/<int:n1>/<int:n2>/<string:tipo>")
def calculadora(n1, n2, tipo):
    if tipo == "suma":
        return str(n1 + n2)

    elif tipo == "resta":
        return str(n1 - n2)

    elif tipo == "multiplicacion":
        return str(n1 * n2)


if __name__ == '__main__':
    appServerWithFlask.run(port=81)
