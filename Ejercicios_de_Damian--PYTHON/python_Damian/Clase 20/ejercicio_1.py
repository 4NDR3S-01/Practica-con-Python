n = int(input("Ingrese un numero para generar las N primeras tablas de multiplicar: "))
while n > 0:
    for i in range(1,n+1):
        if i % 2 == 0:
            for j in range(1,11):
                r = i * j
                print(f"{i} * {j} = {r}")
            print("--------------------")
        else:
            for j in range(15,0,-1):
                r =  i * j
                print(f"{i} * {j} = {r}")
            print("--------------------")
    n = int(input("Ingrese un numero para generar las N primeras tablas de multiplicar (Ingrese un 0 para salir): "))
