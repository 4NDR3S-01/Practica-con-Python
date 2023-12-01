m = 0
v = int(input("Ingrese valores (Se detiene con un 0): "))
while v > 0:
    if v > m:
        m = v
    else:
        v = int(input("Ingrese valores (Se detiene con un 0): "))
print("El numero mayor ingresado es: ", m)