#listo para empezar
mibool = True
numeros=31
string="Hola"

lista=[10,20,30]
print(lista)

if(lista[0]>30):
    print("el numero "+str(lista[0])+" es mayor a 30")
elif(lista[1]>30):
    print("es verdad")
else:
    print(f"el numero {lista[0]} no es mayor a 30")


tupla = (0,1,2,3,4)
tupla2 = ("hola","que","hace")

diccionario={1:"juan",
             2: "miguel",
             "nombre": "pepe",
             "id":1234}
print(diccionario)
diccionario[0]="pedro"
print(diccionario)
diccionario["id"]=4321
print(diccionario)
print(f"nombre {diccionario[2]}")