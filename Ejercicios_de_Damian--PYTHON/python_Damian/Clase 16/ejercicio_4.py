ea = 0
er = 0
n = int(input("Ingrese cuantos estudiantes va a ingresar: "))
if n < 1:
    print("Error")
else: 
    for i in range(n):
        print("Notas del estudiante",i+1)
        n1 = int(input("Ingrese la nota del primer parcial: "))
        n2 = int(input("Ingrese la nota del segundo parcial: "))
        nf = n1 + n2
        if nf >= 14:
            ea += 1
        else:
            er += 1
    print("Total de estudiantes aprobados: ",ea)
    print("Total de estudiantes que va a recuperacion: ",er)