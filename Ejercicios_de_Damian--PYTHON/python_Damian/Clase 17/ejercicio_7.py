s = 0
n = int(input("Ingrese un valor N para resolver esta serie: S = (1/2)^1 + (2/4)^2 + (3/6)^3 + ...... + (N / N*2)^N "))
if n < 1:
    print("Error")
else:
    for i in range(1,n+1):
        s = s + (i / (i*2))**i
    print("El resultado es", s)