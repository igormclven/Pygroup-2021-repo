print("Hola :)")
lista = [10, 20, 30, "hola", True]
[print(x) for x in lista if type(x) == int]
tupla = (1, 2, 3, 4)  # Son inmutables
print(tupla[0])
[print(i) for i in tupla]
dict = {}
