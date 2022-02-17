# este programa contine un ejercicios basado en lo que se vio en clase sobre servicios web con Flask

# este programa es una calculadora más avanzada que la anterior usando partes de la direccion como parametros

from flask import Flask

# cuando no se especifica una peticion se ejecuta el get automaticmente

ejercicioDeClase = Flask(__name__)

# decorador que muestra
@ejercicioDeClase.route("/")
def paginaInicio():
    return "<h1>Buenas, este programa es una calculadora. Miguel Nicolas Diaz Vargas 2022-02-17</h1>"

# funcion para realizar operaciones basicas de calculadora
@ejercicioDeClase.route("/calculadoraBasica/<int:n1>/<int:n2>/<string:tipo>")
def calculadora(n1,n2,tipo):
    if tipo== "suma":
        return str(n1+n2)

    elif tipo == "resta":
        return str(n1 - n2)

    elif tipo == "multiplicacion":
        return str(n1 * n2)

    elif tipo == "division":
        if n2 == 0:
            return "La division no se puede realizar, denominador menor a 0"
        else:
            return str(n1 / n2)

# funcion para saber si un numero es primo o no
@ejercicioDeClase.route("/calculadoraPrimo/<int:numero>/primo")
def calculadoraPrimo(numero):
    primo = True

    for i in range(2, numero, 1):
        if numero % i == 0:
            primo = False

    if primo == True:
        return f"{numero} es primo"
    else:
        return f"{numero} no es primo"

if __name__ == '__main__':
    ejercicioDeClase.run(port=80)