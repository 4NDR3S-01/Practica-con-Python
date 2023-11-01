# Ingresar datos de estudiantes y sus calificaciones
students = {}
while True:
    name = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if name == 'salir':
        break
    score = int(input("Ingrese la calificación del estudiante: "))
    students[name] = score

# Calcular el promedio de calificaciones de un estudiante
def average_score(student):
    total_score = sum(student.values())
    return total_score / len(student)

# Identificar si un estudiante aprobó o reprobó
def pass_fail(student):
    avg = average_score(student)
    if avg >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

# Calcular el promedio general de calificaciones de todos los estudiantes
def class_average(students):
    total_score = 0
    for student in students:
        total_score =+ sum(students[student])
    return total_score / len(students)

# Identificar al estudiante que cuente con el promedio más alto
def highest_average(students):
    highest_avg = 0
    highest_student = ""
    for student in students:
        avg = average_score(students[student])
        if avg > highest_avg:
            highest_avg = avg
            highest_student = student
    return highest_student

# Mostrar cuántos estudiantes aprobaron y cuántos reprobaron
def pass_fail_count(students):
    pass_count = 0
    fail_count = 0
    for student in students:
        if pass_fail(students[student]) == "Aprobado":
            pass_count =+ 1
        else:
            fail_count =+ 1
    return (pass_count, fail_count)

# Ejecutar las funciones y mostrar los resultados
print("Los datos ingresados son: ", students)
print("El promedio de calificaciones es: ", average_score(students))
print("El estudiante ha", pass_fail(students), "la clase.")
print("El promedio general de la clase es: ", class_average(students))
print("El estudiante con el promedio más alto es: ", highest_average(students))
pass_count, fail_count = pass_fail_count(students)
print("Hay", pass_count, "estudiantes aprobados y", fail_count, "estudiantes reprobados.")