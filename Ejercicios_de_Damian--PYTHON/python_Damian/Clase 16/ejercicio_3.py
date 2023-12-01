vp = 0
vc = 0
vn = 0
n = int(input("Ingrese cuantos valores va a ingresar: "))
if n < 1:
    print("Error")
else: 
    for i in range(n):
        v = int(input(f"Ingrese el valor {i+1}: "))
        if v >= 1:
            vp += 1
        else:
            if v <= -1:
                vn += 1
            else:
                vc += 1
    print("Total de numeros positivos: ", vp)
    print("Total de numeros ceros: ", vc)
    print("Total de numeros negativos: ", vn)