def factorial(n):
    #Caso base cuando el usuario ingresa 0
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
    
#Ejemplo de uso 
valor = int(input("Ingrese el valor: \n"))
resultado = factorial(valor)
print(resultado)