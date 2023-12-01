vi = int(input("Ingrese un valor inicial para la multiplicacion: "))
vf = int(input("Ingrese un valor final para la multiplicacion: "))
while vi < vf:
    for i in range(vi,vf+1):
        for j in range(1,11):
            r =  i * j
            print(f"{i} * {j} = {r}")
        print("------------------")
    vi = int(input("Ingrese un valor inicial para la multiplicacion (Ingrese un 0 para salir): "))
    vf = int(input("Ingrese un valor final para la multiplicacion (Ingrese un 0 para salir): "))