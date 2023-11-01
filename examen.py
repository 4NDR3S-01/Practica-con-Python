menu = """
Bienvenido
1. Ingresar al sistema
2. Salir
"""
auxiliar = True
while auxiliar:    
    print(menu)
    op = int(input("Seleccione una opcion del menu: "))
    if op == 1:
        promediodeventas = 0
        montototal = 0
        diaventalta = 0
        ventasuperiores = 0
        diasingresados = int(input("Ingrese cuantos dias va a ingresar: "))
        montodeterminado = int(input("Contar cuantos dias tuvieron ventas superiores al monto de: "))
        for i in range (diasingresados):
            nombredia = str(input(f"Ingrese el dia {i+1} (ej: Lunes) de la venta: "))
            montodeventa = int(input(f"Ingrese el monto de la venta {i+1}: "))
            montototal = montototal + montodeventa
            if montodeventa > montodeterminado:
                ventasuperiores += 1
            if montodeventa > diaventalta:
                diaventalta = montodeventa
                ndiaventalta = nombredia
        promediodeventas = montototal / diasingresados
        print("El monto total de ventas es: ", montototal)
        print(f"El promedio de ventas diarias es: ", promediodeventas)
        print(f"El dia {ndiaventalta}, es el dia con venta mas alta")
        print(f"Tuvieron {ventasuperiores} dias con ventas superiores al monto")
    elif op is 2:
        print("Saliendo del sistema..")
        auxiliar = False
    else:
        print("No ingresaste un valor dentro del menu")
print("Saliste del sistema.")