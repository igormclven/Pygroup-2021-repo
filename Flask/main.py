from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hola mama, estoy en internet!</h1>"

@app.route("/calculadora/<int:n1>/<int:n2>/<string:tipo>")
def calculadora(n1,n2,tipo):
    if tipo== "suma":
        return str(n1+n2)

    elif tipo == "resta":
        return str(n1 - n2)

    elif tipo == "multiplicacion":
        return str(n1 * n2)




# main y port de la app
if __name__ == '__main__':
    app.run(port=80)