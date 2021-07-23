#3. Escribir un programa que pida al usuario un número entero 
#y muestre un mensaje si el número es par o impar.

numero =int(input("Ingrese un numero entero: "))

if numero % 2 == 0:
    print('El número', numero, 'es par.')
else:
    print('El número', numero, 'es impar.')

