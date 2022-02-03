# Este progrma determina si un numero ingresado por el usuario es primo o no

exit = 1

while exit!=0:

    numeroIngresado = int(input("\nIngrese un numero para determinar si este es primo o no, por favor ingresar numeros iguales o mayores a 0: "))
    primo = True

    if numeroIngresado <= 0:
        print("\nEl numero es menor a 0, vuelva a intentar\n")
    else:
        for i in range(2, numeroIngresado, 1):
            if numeroIngresado % i == 0:
                primo = False

        if primo == True:
            print("\nEl numero es primo\n")
        else:
            print("\nEl numero no es primo\n")

    exit = int(input("¿Desea realizar otro proceso? (No = 0 / Si = 1): "))
