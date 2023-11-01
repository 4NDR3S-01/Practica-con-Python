estudiantes = int(input("Cuantas estudiantes vas a ingresar: "))
pg = 0
mp = 0
ea = 0
er = 0
for i in range(estudiantes) :
    nombre = str(input("Ingrese el nombre del estudiante: "))
    calificaciones = int(input("Cuantas calificaciones vas a ingresar: "))
    nf = 0
    for j in range(calificaciones):
        calificacion = int(input("Ingrese la calificacion del estudiante: " ))
        nf = nf + calificacion
    pf = int(nf / calificaciones)
    pg = int(pg + pf)
    if pf >= 70 :
        print("Hola, ",  nombre, ". Tu promedio es: ", pf)
        print("Estudiante ", nombre, ", usted aprobo")
        ea = ea + 1 
        if pf > mp :
            mp = pf
            mayorpromedio = nombre
    else :
        print("Hola, ", nombre, ". Tu promedio es: ", pf)
        print("Estudiante ", nombre, ", usted reprobo")
        er = er + 1
pgf = int(pg / estudiantes)
print("El promedio general de calificaciones de todos los estudiantes es: ", pgf)
print("Estudiante con mayor promedio es :",mayorpromedio )
print("Estudiantes aprobados: ", ea, "Estudiantes reprobados: ", er,)