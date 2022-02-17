#Primer commit de mi rama 15/12/2021
a=15
b=7

lista = []
print(lista)

lista = [10,20,30]
print(lista)

#Lista
lista = [True,20,30]
print(lista[0])

#tupla = valor inmutable, no se puede cambiar
tupla = (1,2,3,4,5)
tupla2 = ('Miguel', 'Nicolas')

#diccionarios = coleccion desordenada de valores, se pueden editar
dict = {1: "Juan"} # un identificador y un dato
dict2 = {1: "Nicolas", 2: "Goku"}
dict3 = {'nombre': 'Nicolas', 2: "Goku"}
print(dict2)
dict[0] = "Pedro" #editarlo
dict["Pedro"] = "no existe" #editarlo
dict3 = {'valores': [1,2,3,4,5]} # un lista dentro de un diccionario

#Estruturas de control
#IF
if (lista[0] == True):
    print('Efectivamente es true')

if (lista[0] > 30):
    print('el num' + lista[0] + 'es mayor a 30')
elif(lista[1] > 30):
    print('Efectivamente es true')
else:
    print('el num' + str(lista[0]) + 'es mayor a 30')
    print('el num {lista[0]} es mayor a 30')

if (a%2)==0:
    print(f'El valor {a} es par')
elif(b%2) == 0:
    print(f'El valor {b} es par')
else:
    print("Ninguno es par")

if (a % 2) == 0 or (b % 2) == 0:
    print('Alguno es par')
else:
    print("Ninguno es par")

#while
a = 8
b = 1
while (a>1):
    a= a-1
    b = b + 2
    print(a,b)

#estructura de ternario
cualquiera = 'pepe' if (b==1) else 'juan'
print(cualquiera)

#for
dias = ["Lun","Mar","Mier"]
for dia in dias:
    print(f'el dia es {dia}')

for i,j in dict.items():
    print(i,j)

for i, j in dict.items():
    print(i, j)
    lista.append(j)

for i in range(11):
  print(i)

for i in range(11):
    if i == 7:
        break
    print(i)

print(lista)


# 2022-02-9 ------------------------------------------------------------------------------

# ---------------------------- FUNCIONES ---------------

# FUNCIONES: Son conjuntos de codigo que son hechas para usarse muchas veces. Buscan ser lo más sencillas posibles
def nombre_funcion (entra_algo):
    opera_algo = entra_algo
    opera_algo =+ opera_algo
    returna_algo = opera_algo
    return returna_algo

# JOIN encadena valores, en este caso el resultados de la funcion imprimirFizzbuzz
def imprimirFizzbuzz (i):
    return i

numeros = "\n".join(imprimirFizzbuzz(i) for i in range (1,101))


# PROCEDIMIENTO: no entran parametros ni retorna
def imprimir():
    print("Me llamaron")

imprimir()

# PASO INDEFINIDO DE PARAMETROS EN FUNCION: nosabemos cuantos parametros van a llegar, solo importa que lleguen argumentos
def suma(*args): # muchos elementos
    result = 0
    for i in args:
        result = result + i
    return result

print(suma(1,2,3,4,5,6,7,8,9,10))

# 2022-02-16 ------------------------------------------------------------------------------

# ---------------------------- uso de servicios web con FLASK ---------------

from flask import Flask

app = Flask(__name__)

## Decorador que define la ruta donde va a parecer la funcion siguiente
@app.route("/")
def funcionDeInicio():
    return "<h1>Hola mama, estoy en internet!</h1>"   #aqui ya podemos usar html

# toma partes del enlace como parametros
@app.route("/calculadora/<int:n1>/<int:n2>/<string:tipo>")
def calculadora(n1,n2,tipo):
    if tipo== "suma":
        return str(n1+n2)

    elif tipo == "resta":
        return str(n1 - n2)

    elif tipo == "multiplicacion":
        return str(n1 * n2)

## main y port de la app
if __name__ == '__main__':
    app.run(port=80)























