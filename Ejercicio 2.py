#2. Escribir un programa que pida al usuario dos números 
#realizar la división entre estos dos y mostrar el resultado. 
#Si el divisor es cero el programa debe mostrar un error.

x =int(input("Ingrese el dividendo: "))
y =int(input("Ingrese el divisor: "))

if y >=1:
    print(f"Su resultado es: {x/y}")
else:
  if y == 0:
      print("Error")



