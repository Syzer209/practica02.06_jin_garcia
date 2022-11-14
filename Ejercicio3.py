producto = {"Pan": 1.40, "Huevos": 2.30, "Cebolla": 0.85, "Aceite": 4.35}
articulo = input("Introduce el articulo deseado: ")
unidad = int(input("Introduce la unidad deseada: "))
if articulo in producto:
    print(float((producto[articulo] * unidad)))