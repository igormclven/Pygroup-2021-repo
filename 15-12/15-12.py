#colecciones

# 1. Tuplas,2. Listas,3. Set,4. Diccionarios

lista = []
print(lista)

lista = [10,20,15,36,88]
print(lista)

lista = ["hoa","prueba",2,"WoW"]
print(lista)
print(lista[1])

if (lista[2] == "2"):
    print("Si imprime esto python tiene huevo")
else:
    print("")
    print("Menos mal xd")
    print("el valor de la posicion de 0 es: " + str(lista[0]))
    #OTRA FORMA (SALIDA FORMATEADA)
    print(f"el valor de la posición de 1 es: {lista[1]}")

#TUPLAS :)

tupla = (0,1,2,3,4,5)
tupla2 = ("hello","mother","pretty")

#DICCIONARIO

dict = {1: "Juan",
        2: "Pedro",
        "id": 98}
print(dict)

dict[0] = "hostia"
dict[1] = 4568891
print(dict)
print(dict["id"])

# While

a = 8
b = 1

while (a<=15):
    print(f"Soy un ciclo while y valgo: {a}")
    a+=1

#Ternario

t = 20

variable = False if(t!=20) else True
print(variable)

#for

dias = ["Lunes","Martes","Miercoles"]

for dia in dias:
    print(f"El dia de hoy es: {dia}")

for i,j in dict.items():
    print(i,j)

for i in range(11):
    print(i)