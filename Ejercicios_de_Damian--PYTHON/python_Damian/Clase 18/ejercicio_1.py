s = 0
n = int(input("Ingrese un valor N para resolver esta formula: S = (1+1) + (2+2) + (3+3) + ...... + (N + N) "))
while n > 1:
    for i in range(1,n+1):
        s = s + (i + i)
    print("El resultado es", s)
    n = int(input("Ingrese un valor N positivo para resolver esta formula: S = (1+1) + (2+2) + (3+3) + ...... + (N + N) "))