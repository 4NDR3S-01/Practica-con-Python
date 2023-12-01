s = 0
n = int(input("Ingrese un valor: "))
if n < 1:
    print("Error")
else:
    for i in range(1,n+1):
        if i % 2 == 0:
            s = s + i
    print("La sumatoria de los N primeros numeros pares es: ", s)