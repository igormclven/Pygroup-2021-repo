from flask import Flask, request

app = Flask(__name__)

estudiantes = []


@app.route("/")
def funcionDeInicio():
    return "<h1>Hello World</h1>"


@app.route("/crear", methods=["POST"])
def createStudent():
    if request.method == "POST":
        estudiante = dict({'codigo': request.form['cod'], 'nombre': request.form['name']})
        estudiantes.append(estudiante)
    return "ok"


@app.route("/lista", methods=["GET"])
def listStudent():
    if request.method == "GET":
        value = ""
        for estudiante in estudiantes:
            values = value + " " + (estudiante['nombre'])
        return value

@app.route("/modify/<string:codigo>", methods=["PUT"])
def modifyStudent(codigo):
    if request.method == "PUT":
        for estudiante in estudiantes:
            if codigo in estudiante["codigo"]:
                estudiante.update(dict({'nombre': request.form['name']}))
            return "ok"
        return "F"

@app.route("/delete/<string>:codigo", methods=["DELETE"])
def deleteStudent(codigo):
    if request.method == "DELETE":
        for estudiante in estudiantes:
            value = 0
            if codigo in estudiante["codigo"]:
                estudiante.remove(value)
            value = value + 1
            return "ok"
        return "F"



if __name__ == '__main__':
    app.run()
