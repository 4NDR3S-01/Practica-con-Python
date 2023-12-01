# Busqueda lineal
#def lineal_busqueda(Lista, buscado):
#    tires=0
#    for i, value in enumerate(lista):
#        tires += 1
#        if value == buscado:
#            return tires, i
#    return tires, -1 
#
#lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
#         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#         'v', 'w', 'x', 'y', 'z'] 
#
#tires, positions = lineal_busqueda(lista, "g")
#
#if positions != -1:
#    print("Coincidencia en la posicion {}, en {} intentos".format(positions, tires))
#else:
#    print("No se encontraron coincidencia")
# Busqueda binaria
def busqueda_binaria(Lista, buscado):
    tires=0
    izq=0
    der=len(lista) -1

    while izq <= der:
        tires += 1
        mitad=(izq+der)//2

        if lista[mitad] == buscado:
            return tires, mitad
        if lista[mitad] > buscado:
            der=mitad-1
        if lista[mitad] < buscado:
            izq=mitad+1
    return  tires, -1



lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z'] 

tires, positions = busqueda_binaria(lista, "z")

if positions != -1:
    print("Coincidencia en la posicion {}, en {} intentos".format(positions, tires))
else:
    print("No se encontraron coincidencia")