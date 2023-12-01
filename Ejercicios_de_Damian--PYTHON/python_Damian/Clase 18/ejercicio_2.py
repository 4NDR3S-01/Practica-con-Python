s = 0
n = int(input("Ingrese un valor n para resolver esta formula: S = A^1 + A^3 + A^5 + ...... + A ^ N "))
while n > 1 and n % 2 == 1:
    a = int(input("Ingrese un valor A: "))
    if a >= 1 and a <= 9:
        for i in range(1,n+1):
            if i % 2 == 1:
                s = s + (a ** i)
        print("El resultado es", s)
    n = int(input("Ingrese un valor n para resolver esta formula: S = A^1 + A^3 + A^5 + ...... + A ^ N) "))