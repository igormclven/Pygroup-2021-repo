#booleanos
mibool = True #if, while

#numeros
numero = 123456

#string
string = "SDGDSF"

#colecciones
tupla = ((1,2),(3,4),(5,6))
lista = [1,True,3,4,"cinco"]
lista2 = [10,20,30,40,50]
sets = []
dicc = {'nombre' : "Julian",'edad' : 23}

print(lista)
print(dicc['nombre'])

#Estructuras de control
#if/else/elif
if (lista[1] == True):
    print("Efectivamente es true")
else:
    print("No es true")

if (lista2[0] > 30):
    print("El num"+ str(lista2[0]) +" es mayor a 30")
elif (lista2[1] > 30):
    print("El num"+ str(lista2[1]) +" es mayor a 30")
else:
    print(f"El num {lista2[0]} no es mayor a 30")

a = 5
b = 10
if (a % 2) == 0 or (b % 2) == 0:
    if (a % 2) == 0:
        print(f"El valor {a} es par")
    else:
        print(f"El valor {b} es par")
else:
    print("Ninguno es par")

#input
"""a = int(input("Ingrese el valor para a: "))
b = int(input("Ingrese el valor para b: "))

if (a % 2) == 0 or (b % 2) == 0:
    if (a % 2) == 0:
        print(f"El valor {a} es par")
    if (b % 2) == 0:
        print(f"El valor {b} es par")
else:
    print("Ninguno es par")
"""
#while
a = 8
b = 1
while(a>1):
    b = b + 2
    a = a - 1
    print(a,b)

#################
cualquiera = 'pepe' if (b == 15) else 'juan'
print(cualquiera)
#################

#for
for a in lista2:
    if a > 30:
        print(f"{a} Es mayor a 30")
    else:
        print(f"{a} No es mayor a 30")

dias = ["lun","mar","mier"]
for dia in dias:
    print(f"El día es {dia}")

for i in range(11):
    print(i)