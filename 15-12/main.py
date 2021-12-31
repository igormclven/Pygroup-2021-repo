# Prueba Python estructuras de datos
mibool = True #if, while
numeros = 33443 #for
string = "kdfjdkf" #if, while, for

#LISTAS (Las listas son mutables y pueden variar en tiempo de ejecucuión)
lista = []
print(lista)

lista = [10, 20, 30]
print(lista)


if (lista[0] > 30):
    print('El num'+ lista[0] +'es mayor a 30')
elif (lista[1] > 30):
    print('Efectivamente es true')
else:
    print('El num ' + str(lista[0]) + ' no es mayor a 30')
    print(f'El num {lista[0]} no es mayor a 30.')

print('Nada que ver xd')

#TUPLAS (Las tuplas son inmutables y no pueden variar en tiempo de ejecución)
tupla = (0,1,2,3,4)
tupla2 = ('hola', 'juancarlos')


#Los diccionarios utilizan clave:valor
dict = {1: 'Juan',
        2: 'Miguel',
        'nombre': 'Pepe',
        'id': 1121212,
        'valores': [1,2,2,3,3]}

print(dict)

dict[0]='Pedro'
dict[1]='Pedro'
dict['id']='id no ext'
print(dict['nombre'])
print(dict['valores'][0])


a = 1
b = 2

if ((a % 2) ==0 or (b % 2) ==0):
    if (a % 2) ==0:
        print(f'{a} es par')
    if (b % 2) ==0:
        print(f'{b} es par')
else:
    print("Ninguno es par")


#########################################
a = 8
b = 1


while (a>1):
    b = b + 2
    a = a -1
    print(a,b)

cualquiera = 'pepe' if (b==15) else 'juan'

print(cualquiera)


#############################################
dias = ['Lun', 'mar', 'mier']

for dia in dias:
    print(f'El dia es {dia}')

print(len(dias))
print(dias[0])
print(dias[1])
print(dias[2])
lista2 = []

# Cuando se recorre un diccionario con for item in dic:, item contiene las claves, no los valores

#Recorrer un diccionario con los valores
for i,j in dict.items():
    print(i,j)
    lista2.append(j)

for j in range(11):
    if j == 7:
        break
    print(j)

print(lista2)
print(lista2[4][3])