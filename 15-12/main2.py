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

a=1
b=2
if(a%2)==0:
    print(f"El valor {a} es par")
elif(b%2)==0:
    print(f"El valor {b} es par")
else:
    print("Ninguno es par")


a=8
b=1
while(a>4):
    b=b+2
    a=a-1
    cualquiera="pepe" if(b==3) else "juan"
    print(cualquiera)


dias=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
for dia in dias:
    print(f"el dia es {dia}")

print(len(dias))

for i,j in diccionario.items():
    print(i,j)

for i in range(4):
    if(i==2):
        break
    print(i)