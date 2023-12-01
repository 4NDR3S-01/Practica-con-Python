s = 0
n = int(input("Ingrese un valor N para resolver esta serie: (S = 1^1 + 2^2 + 3^3 + ...... + N ^ N) "))
if n < 1:
    print("Error")
else:
    for i in range(1,n+1):
        s = s + i ** i 
    print("El resultado es", s)