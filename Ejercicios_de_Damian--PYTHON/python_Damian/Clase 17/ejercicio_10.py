n = int(input("Ingrese un numero: "))
if n < 1:
    print("Error")
else:
    s = 0
    for i in range(1,n):
        if n % i == 0:
            s = s + i
    if s > n:
        print("Es numero abundante")
    else:
        print("No es numero abundante")