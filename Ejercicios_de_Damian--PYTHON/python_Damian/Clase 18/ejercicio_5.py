n = int(input("Ingrese un valor para calcular cuantos digitos tiene: "))
while n >= 0 and n <= 9999:
    if n >= 0 and n < 10:
        print("Tiene 1 digito")
    elif n >= 10 and n < 100:
        print("Tiene 2 digitos")
    elif n >= 100 and n < 1000:
        print("Tiene 3 digitos")
    elif n >= 1000 and n < 10000:
        print("Tiene 4 digitos")
    n = int(input("Ingrese un valor para calcular cuantos digitos tiene (Para detener ingrese un valor mayor a 9999): "))