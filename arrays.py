mi_lista=['Juan', 'Andres','Maria', 'Carmen', 'Jennifer']
for nombres in mi_lista:
    print(nombres)

print('---------------------------')
print('Accediendo a los elementos')
for nombres in mi_lista:
    print(nombres)


print('---------------------------')
print('Accediendo a los indices con while')
indice=0
while indice < len(mi_lista):
    print(indice)
    indice += 1


#Agregar elementos a una lista
nuevo_dato = input("Ingrese un nombre: ")
mi_lista.append(nuevo_dato)

#Recorriendo los elementos
print('Accediendo a los elementos')
for nombres in mi_lista:
    print(nombres)
