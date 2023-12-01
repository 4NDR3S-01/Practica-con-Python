s = 0
n = int(input("Ingrese un numero N para realizar la siguiente formula: S=1!+2!+3!+.....+N! "))
while n > 0:
    for i in range(1,n+1):
        f = 1
        for j in range(1,i+1):
            f = f * j
        s = s + f
    print("El resultado es: ", s)
    n = int(input("Ingrese un numero N para realizar la siguiente formula: S=1!+2!+3!+.....+N! (Ingresa un 0 paraa salir) "))