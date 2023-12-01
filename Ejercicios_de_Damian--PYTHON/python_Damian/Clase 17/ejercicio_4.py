sp = 0
si = 0
st = 0
n = int(input("Ingrese el numero de valores a ingresar: "))
if n < 1:
    print("Error")
else:
    for i in range(n):
        v = int(input(f"Ingrese el valor {i+1}: "))
        st = st + v
        if v % 2 == 0:
            sp = sp + v
        else:
            si = si + v
    print("La suma de los valores pares ingresados es: ", sp)
    print("La suma de los valores impares ingresados es: ", si)
    print("La suma total de los valores ingresados es: ", st)