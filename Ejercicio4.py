diccionario = {}
continuar = True
while continuar:
    clave = input("¿Que dato deseas agregar?: ")
    valor = input(clave + " => ")
    diccionario[clave] = valor
    print(diccionario)
    continuar = input("¿seguir introduciendo datos?: ") == "si".upper()