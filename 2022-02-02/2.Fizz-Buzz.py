#Este programa imprime numeros del 1 al 100, pero si este numero es divisible por 3 y por 5 imprime un mensaje o si es divisible solo por 3 imprime otro y si es divisible por 5 uno distinto

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('Fizz-Buzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)