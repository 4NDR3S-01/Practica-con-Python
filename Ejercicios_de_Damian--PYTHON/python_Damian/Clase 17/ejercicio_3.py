smayor = 0
smenor = 0
empleados = int(input("Ingrese la cantidad de empelados: "))
if empleados < 1 :
    print("Error")
else:
    ts = 0
    esmenor = 0
    esmayor = 0
    for i in range(1,empleados+1):
        sueldo = int(input(f"Ingrese el sueldo mensual del empleado {i}: "))
        ts = ts + sueldo
        if sueldo > 450:
            esmayor += 1
            smayor = smayor + sueldo
        else:
            esmenor += 1
            smenor = smenor + sueldo
    psmayor = smayor / esmayor
    psmenor = smenor / esmenor
    print("El promedio de los sueldos mayores al salario minimo es: ", psmayor)
    print("El promedio de los sueldos menores al salario minimo es: ", psmenor)
    print("El sueldo total de ingresados es: ", ts)