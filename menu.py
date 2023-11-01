# Declaro una constante
menu = """
Bienvenido a mi sistema de calculadora
Elija una opcion del menu 
1.- Sumar
2.- Restar
3.- Multiplicar
4.- Dividir
5.- Salir del sistema
"""
# Variable auxiliar
auxiliar = True
# Bucle
while auxiliar:
    # Imprimo por consola la constante
    print(menu)
    # Solicitar que elija una opcion del menu
    op = int(input("Dime tu opcion del menu: "))
    # Estructurar el menu 
    if op is 1:
        n = int(input("Cuantas operaciones va a realizar: "))
        for i in range(n):
            a = int(input(f"Ingrese el primer valor de la operacion {i+1}: "))
            b = int(input(f"Ingrese el segundo valorde la operacion {i+1}: "))
            if a > 0 and b > 0:
                sum = a + b
                print("La suma es: ", + sum)
            else:
                print("Los valores deben ser positivo")
    elif op is 2:
        n = int(input("Cuantas operaciones va a realizar: "))
        for i in range(n):
            a = int(input(f"Ingrese el primer valor de la operacion {i+1}: "))
            b = int(input(f"Ingrese el segundo valorde la operacion {i+1}: "))
            if a > 0 and b > 0:
                if a > b:
                    rest = a - b
                    print("La resta es: ", + rest)
                else:
                    print("El primer valor debe ser mayor que el segundo")
            else:
                print("Los valores deben ser positivo")
    elif op is 3:
        n = int(input("Cuantas operaciones va a realizar: "))
        for i in range(n):
            a = int(input(f"Ingrese el primer valor de la operacion {i+1}: "))
            b = int(input(f"Ingrese el segundo valorde la operacion {i+1}: "))
            if a >0 and b > 0:
                mult = a * b
                print("La multiplicacion es: ", + mult)
            else:
                print("Los valores deben ser positivo")
    elif op is 4:
        n = int(input("Cuantas operaciones va a realizar: "))
        for i in range(n):
            a = int(input(f"Ingrese el primer valor de la operacion {i+1}: "))
            b = int(input(f"Ingrese el segundo valorde la operacion {i+1}: "))
            if a > 0 and b > 0 :
                if b == 0:
                    print("No se puede dividir entre cero")
                else:
                    div = a / b
                    print("La division es: ", + div)
            else:
                print("Los valores deben ser positivo")
    elif op is 5:
        print("Saliendo del sistema...")
        auxiliar = False
    else:
        print("No ingresaste una opcion dentro del menu")
print("Saliste del sistema.")