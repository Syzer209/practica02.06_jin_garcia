alumnos_diccionario = {}
opcion = input("Eliga una opción:"
               "(1) Añadir alumno/a, "
               "(2) Eliminar alumno/a, "
               "(3) Mostrar alumno/a, "
               "(4) Listar todo el alumnado, "
               "(5) Listar alumnado aprobado, "
               "(6) Terminar  ")

while opcion != "6":
   if opcion == "1":
       nif = input("Introduzca su NIF: ")
       nombre = input("Introduzca su nombre: ")
       telefono = input("Introduzca su número de teléfono: ")
       correo = input("Introduzca su correo electrónico: ")
       modulo = input("¿Ha aprobado el módulo?: ")
       alumnos_nota = {"nombre": nombre, "telefono": telefono, "correo": correo, "modulo": modulo == "si"}
       alumnos_diccionario[nif] = alumnos_nota

   if opcion == "2":
       nif = input("Introduzca su NIF: ")
       if nif in alumnos_diccionario:
           del alumnos_diccionario[nif]
       else:
           print("No se encuentra su NIF")
   if opcion == "3":
       nif = input("Introduzca su NIF: ")
       if nif in alumnos_diccionario:
           for clave, valor in alumnos_diccionario[nif].items():
               print(clave.title(),":", valor)
       else:
           print("No se encuentra su NIF")
   if opcion == "4":
       for clave, valor in alumnos_diccionario.items():
           print(clave, valor['nombre'])
   if opcion == "5":
       for clave, valor in alumnos_diccionario.items():
           if valor["modulo"]:
               print(clave, valor["nombre"])
   opcion = input("Eliga una opción:"
                  "(1) Añadir alumno/a, "
                  "(2) Eliminar alumno/a, "
                  "(3) Mostrar alumno/a, "
                  "(4) Listar todo el alumnado, "
                  "(5) Listar alumnado aprobado, "
                  "(6) Terminar ")