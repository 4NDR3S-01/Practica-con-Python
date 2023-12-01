np = 0
ni = 0
n = int(input("Ingrese cuantos valores va a ingresar: "))
if n < 1:
    print("Error")
else: 
    for i in range(n):
        v = int(input(f"Ingrese el valor {i+1}: "))
        if v < 1:
            print("Error")
        else:
            r = v % 2
            if r == 0:
                np += 1
            else:
                ni += 1
    print("Total de numeros pares: ", np)
    print("Total de numeros impares: ", ni)