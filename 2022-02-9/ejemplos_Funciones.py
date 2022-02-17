# Funciones: Son conjuntos de codigo que son hechas para usarse muchas veces
def nombre_funcion (entra_algo):
    opera_algo = entra_algo
    opera_algo =+ opera_algo
    returna_algo = opera_algo
    return returna_algo



import random
Nombre = ["Juan", "Daniela"]
Premios = ["ha ganado barrer la casa", " se gano lavar la loza"]

def asignacion (nombre, tarea):
    print (f" a {nombre} le toca hacer {tarea}")

asignacion (Nombre[random.randint(0,4)], Premios[random.randint(0,3)])



def potencia(valor, n):
    result = valor

    for i in range (1,n):
        result = result * valor
    return result

print(potencia(17,4))

# PROCEDIMIENTO: no entran parametros ni retorna
def imprimir():
    print("Me llamaron")

imprimir()


# PASO INDEFINIDO DE PARAMETROS EN FUNCION: nosabemos cuantos parametros van a llegar, solo importa que lleguen argumentos
def suma(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(suma(1,2,3,4,5,6,7,8,9,10))
