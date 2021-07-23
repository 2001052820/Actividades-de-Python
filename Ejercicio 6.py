#1. solicite un correo
#2. si el correo es hotmail solicite nombre y apellido y los imprima en pantalla
#3. si el correo es gmail solicite el nombre  y la edad y las imprima en pantalla
#4. si el correo es yahoo solicite el tipo y número documento 

correo = input("ingrese su correo: ")

a = correo.rfind("hotmail") 
d = correo.rfind("gmail")

if a:
    print( input("ingrese nombre y apellido: "))
    
    print(f"su nombre y apellido son {input}")
else :
    print( input("ingrese nombre y edad: "))