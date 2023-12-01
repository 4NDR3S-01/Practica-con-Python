s = 0
n = int(input("Ingrese un valor n para resolver esta formula: S = A^N + A^N*1 + A^N*2 + ...... + A ^ N * N "))
while n >= 0:
    a = int(input("Ingrese un valor A: "))
    while a >= 1 and a <= 9:
        s = a ** n
        for i in range(1,n+1):
            s = s + (a ** (n * i))
        print("El resultado es", s)
        n = int(input("Ingrese un valor n para resolver esta formula: S = A^N + A^N*1 + A^N*2 + ...... + A ^ N * N "))
        a = int(input("Ingrese un valor A: "))