from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return f"<h1c> Hola {nombre}<h1>"

@app.route('/suma/<int:n1>/<int:n2>')
def suma(n1,n2):
    return f"<h1> {n1} + {n2} = {n1+n2}<h1>"

@app.route('/resta/<int:n1>/<int:n2>')
def resta(n1,n2):
    return f"<h1> {n1} - {n2} = {n1-n2}<h1>"

@app.route('/multiplicacion/<int:n1>/<int:n2>')
def multiplicacion(n1,n2):
    return f"<h1> {n1} * {n2} = {n1*n2}<h1>"

@app.route('/divicion/<int:n1>/<int:n2>')
def divicion(n1,n2):
    if n2==0:
        return "<h1> No se puede dividir por cero"
    return f"<h1> {n1} / {n2} = {n1/n2}<h1>"