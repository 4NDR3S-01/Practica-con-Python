f = 1
n = int(input("Ingrese un valor para calcular el factorial: "))
for i in range(1,n+1):
    f = f * i
print(f"El factorial de {n}! es: ", f)