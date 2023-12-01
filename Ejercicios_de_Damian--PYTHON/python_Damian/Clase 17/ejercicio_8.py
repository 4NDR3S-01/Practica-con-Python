s = 0
n = int(input("Ingrese un valor N para resolver esta serie: S = (1/2)^2 + (2/4)^4 + (3/6)^6 + ...... + (N / N*2) ^ N*2 "))
if n < 1:
    print("Error")
else:
    for i in range(1,n+1):
        s = s + (i / (i*2))**(i*2)
    print("El resultado es", s)