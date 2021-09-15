menu = """"
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos
4 - Pesos yuan

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿Cuántos pesos colombianos tienes?:")
    pesos = float (pesos)
    valor_dolar = 3803
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

elif opcion == 2:
    pesos = input("¿Cuántos pesos argentinos tienes?:")
    pesos = float (pesos)
    valor_dolar = 97,87
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")

elif opcion == 3:
    pesos = input("¿Cuántos pesos mexicanos tienes?:")
    pesos = float (pesos)
    valor_dolar = 19,89
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")
elif opcion == 4:
    pesos = input("¿Cuántos pesos yuan tienes?:")
    pesos = float (pesos)
    valor_dolar = 6,45
    dolares = pesos / valor_dolar
    dolares = round(dolares,1)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dolares")


else:
    print("Ingresa una opción correcta por favor")



