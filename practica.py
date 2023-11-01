#Declaramos las listas
nombres=[]
identificaciones=[]

#Tamaño
tamanio = 3

#Ingreso de datos
for i in range(tamanio):
    print("Ingrese los dattos de la persona: ", i+1)
    #Solicitamos los datos por teclado
    nombre = input("Nombre: ")
    identificacion = input("Indentificacion: ")
    #Agregamos los datos a las listas
    nombres.append(nombre)
    identificaciones.append(identificacion)

#Mostrar la informacion almacenada
for i in range(tamanio):
    print("Mostrando los datos de la persona ", i+1)
    print("Nombre: ", nombres[i])
    print("Indentificacion: ", identificaciones[i])

eliminari = nombres.pop(int(input("Ingrese el indice a eliminar: ")))
print("El nombre eliminado es: ", eliminari)
print("La nueva lista", nombres)

eliminare = nombres.remove(input("Ingrese el nombre a eliminar: " ))
print("El nombre eliminado es: ", eliminare)
print("La nueva lista", nombres)