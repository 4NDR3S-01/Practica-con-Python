interruptor = True
while interruptor: 
    v = int(input("Ingrese un valor "))
    if v < 2:
        interruptor = False
    else:
        c = 0
        for i in range(1,v+1):
            if v % i == 0:
                c += 1
        if c == 2:
            print("El numero es primo") 
        else:
            print("El numero no es primo")
