#el programa se encarga de elegir al azar al ganador para hacer aseo a la oficiona de una lista he imprimirlo

import random

listaNombres = ['Nicolas','Camila','Fernanda','Cristian','Mauricio','Natalia','Dayana','Daniela','Danna']

turno = random.choice(listaNombres);

print(turno + ' es el ganador de hacer el aseo en la oficina')