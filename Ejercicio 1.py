#1. Escribir un programa que pregunte al usuario su nombre y su edad, 
#si es mayor de edad pida el numero de cedula y muestre el nombre, la edad y el número de cédula ingresado, 
#si no es mayor de edad, debe mostrar un mensaje que diga Lo siento Pepito, eres menor de edad.

nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))

if edad > 18: #mayor de edad
    cedula = int(input("Ingrese su numero de cedula: "))
    print(f"Su nombre es: {nombre} su edad es {edad} su numero de cedula es {cedula}")
else:
    print(f"Lo siento {nombre} eres menor de edad")
