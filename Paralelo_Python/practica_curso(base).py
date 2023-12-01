import os

lista_de_estudiantes = []
formato = ".txt"

def crear_curso():
    nombre_del_curso = input("Ingrese el nombre del curso: ") + formato
    with open(nombre_del_curso, "w") as file:
        respuesta = str(input("Desea agregar estudiantes (si - no): "))
        if respuesta.lower() == "si":
            estudiantes = int(input("Ingrese la cantidad de estudiantes a ingresar: "))
            for i in range(estudiantes):
                nombre_del_estudiante = input("Ingrese el nombre del estudiante: ")
                lista_de_estudiantes.append(nombre_del_estudiante)
            for estudiante in lista_de_estudiantes:
                file.write(estudiante + '\n')
            print(f"Curso creado exitosamente.\nCon el nombre de: {nombre_del_curso}")
        elif respuesta.lower() == "no":
            print(f"Muchas gracias.\nCreaste un archivo llamado {nombre_del_curso}")

def modificar_curso():
    nombre_del_curso = input("Ingrese el nombre del archivo a modificar: ") + formato
    if not os.path.exists(nombre_del_curso):
        print("No hay un curso creado.\nPor favor, cree un curso primero.")
        return
    with open(nombre_del_curso, "r") as file:
        contenido = file.read()
    print("Lista de estudiantes actual del curso:\n", contenido)
    nueva_lista = input("Ingrese la nueva lista de estudiantes del curso: ")
    with open(nombre_del_curso, "w") as file:
        estudiantes = int(input("Ingrese la cantidad de estudiantes a ingresar: "))
        for i in range(estudiantes):
            nombre_del_estudiante = input("Ingrese el nombre del estudiante: ")
            file.write(nombre_del_estudiante + "\n")
    print("Curso modificado exitosamente.")

def visualizar_curso():
    nombre_del_curso = input("Ingrese el nombre del curso a visualizar: ") + formato
    if not os.path.exists(nombre_del_curso):
        print("No hay un curso creado con ese nombre. Por favor, cree un curso primero.")
        return
    with open(nombre_del_curso, "r") as file:
        contenido = file.read()
    print("La lista de estudiantes:\n", contenido)

menu = """
Hola, Bienvenido al sistema de crear cursos
1. Crear curso
2. Modificar curso
3. Visualizar curso
4. Salir"""

while True:
    print(menu)
    opcion = input("Seleccione una opción (1 al 4): ")
    if opcion == "1":
        crear_curso()
    elif opcion == "2":
        modificar_curso()
    elif opcion == "3":
        visualizar_curso()
    elif opcion == "4":
        print("Saliendo del programa...........")
        break
    else:
        print("Por favor ingrese un número del 1 al 4.")