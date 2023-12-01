a = 0
c = 0
v = int(input("Ingrese valores (Se detiene con un 0): "))
while v > 0:
    a = a + v
    c += 1
    v = int(input("Ingrese valores (Se detiene con un 0): "))
pa = a / c
print("El promedio aritmetico de los valores ingresados es: ", pa)