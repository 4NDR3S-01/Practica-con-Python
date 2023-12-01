s = 0
n = int(input("Ingrese un valor N para resolveresta serie: S= (1 + 2 + 3 + ...... + N) / N "))
if n < 1:
    print("Error")
else:
    for i in range(1,n+1):
        s = (s + i)
        r = s / n
    print("El resultado es", r)