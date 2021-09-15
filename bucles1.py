def run():
    LIMITE = 1000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + 
              "es igual a: "  +  str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "_main_":
    run()

#llegamos al entrypoint que es el if python encuentra la segunda linea y va 
# a ejecutar la funcion run
# en la funcion run se define una constante que se llama LIMITE que tiene el valor de 1000
# se define una variable que se va a llamr contador que tiene valor de 0 
# la segunda variable es potencia_2 que va tener el valor de 2 elevado a contador 
#  y vamos a decir mientras la potencia de 2 sea menor al limite,vamos a ejecutar codigo 
#imprimimos 2 elevado a 0 es igual a 1,contador ahora vale 1 y potencia_2 ahora vale 2 elevado a 1 vale 2 
# y se ejecuta de manera repetida hasta que la condicion deje de cumplirse
#  