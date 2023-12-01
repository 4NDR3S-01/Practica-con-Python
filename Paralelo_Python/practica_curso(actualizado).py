import os

formato = ".txt"

def crear_curso():
    nombre_del_curso = input("Ingrese el nombre del curso: ") + formato
    respuesta = input("Desea agregar estudiantes (si - no): ").lower()
    if respuesta == "si":
        estudiantes = int(input("Ingrese la cantidad de estudiantes a ingresar: "))
        lista_de_estudiantes = [input("Ingrese el nombre del estudiante: ") for _ in range(estudiantes)]
        with open(nombre_del_curso, "w") as file:
            file.write('\n'.join(lista_de_estudiantes))
        print(f"Curso creado exitosamente.\nCon el nombre de: {nombre_del_curso}")
    elif respuesta == "no":
        with open(nombre_del_curso, "w") as file:
            print(f"Muchas gracias.\n Se creo el curso con el nombre de: {nombre_del_curso}")

def modificar_curso():
    cursos_disponibles = [curso for curso in os.listdir('.') if curso.endswith(formato)]

    if not cursos_disponibles:
        print("No hay cursos disponibles. Por favor, cree un curso primero.")
        return

    print("Cursos disponibles:")
    for curso in cursos_disponibles:
        print(f"* {curso}")

    nombre_del_curso = input("Ingrese el nombre del curso a modificar: ") + formato
    if not os.path.exists(nombre_del_curso):
        print("No hay un curso creado.\nPor favor, cree un curso primero.")
        return
    with open(nombre_del_curso, "r") as file:
        contenido = file.read()
    print("Lista de estudiantes actual del curso:\n", contenido)
    nueva_lista = '\n'.join(input("Ingrese el nombre del estudiante del curso: ") for i in range(int(input("Ingrese la cantidad de estudiantes a ingresar: "))))
    with open(nombre_del_curso, "w") as file:
        file.write(nueva_lista)
    print("Curso modificado exitosamente.")

def visualizar_curso():
    cursos_disponibles = [curso for curso in os.listdir('.') if curso.endswith(formato)]
    if not cursos_disponibles:
        print("No hay cursos disponibles. Por favor, cree un curso primero.")
        return

    print("Cursos disponibles:")
    for curso in cursos_disponibles:
        print(f"* {curso}")

    nombre_del_curso = input("Ingrese el nombre del curso a visualizar: ") + formato
    if not os.path.exists(nombre_del_curso):
        print("No hay un curso creado con ese nombre. Por favor, cree un curso primero.")
        return
    with open(nombre_del_curso, "r") as file:
        contenido = file.read()
    print("La lista de estudiantes:\n", contenido)

menu = """
Hola, Bienvenido al sistema de "CREAR CURSO"
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