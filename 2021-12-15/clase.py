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