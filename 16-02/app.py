from Flask import flask

app = Flask(__name__)

@app.route("/")
def funcionDeInicio():
    return "<h1>Hello World</h1>"

@app.route("/saludo/<string:nombre>")
def funcionSaludo(nombre):
    return f"Hola {nombre}"

@app.route("calculadora/<int:n1>/<int:n2>/<string:tipo>")
def calculadora(n1,n2,tipo):
    if tipo == 'suma':
        return n1+n2

    if tipo == 'resta':
        return n1-n2

    if tipo == 'mult':
        return n1*n2

if __name__ == '__main__':
    app.run(port=80)