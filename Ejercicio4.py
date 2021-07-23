#4. Escribir un programa que pida al usuario que ingrese una contraseña, 
# luego solicitar que escriba de nuevo la contraseña, 
# imprimir un mensaje que indique si la contraseña coincide o no.

contraseña = str(input("Ingrese su contraseña: "))
confirmacion = str(input("Ingrese otra vez la contraseña: "))

if contraseña == confirmacion:
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")







