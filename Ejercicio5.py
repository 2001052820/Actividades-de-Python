#5. Escribir un programa que solicite al usuario un carácter y, 
# si se ingresa mas de un carácter, imprimir un mensaje que indique que solo debe ser un carácter.
# si se ingresa un solo carácter y ese carácter es una vocal imprimir el mensaje “es una vocal”. 

caracter = str(input("Ingrese un carácter: "))

if len(caracter)!=1:
    print("Debe ser sólo un carácter")
else:
    if caracter in "aeiou":
        print("Es una vocal")


        
    
