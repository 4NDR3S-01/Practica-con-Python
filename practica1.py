nombre = []
identificaciones = []
cantidad_personas = int(input('Ingrese cantidad de personas: '))
print('Por favor infrese los nombre de las personas y sus identicaión')

for i in range(cantidad_personas):
    print('Ingrese nombre de la persona ', i+1)

    nom=input('nombre: ')
    ide=input('Identiciación: ')
    nombre.append(nom)
    identificaciones.append(ide)
opcion = input('Desea eliminar un dato por índice (i) o por valor (v)? ')
if opcion.lower() == 'i':
     indice_eliminar = int(input('Ingrese el indice a eliminar: '))
     if indice_eliminar >= 1 and indice_eliminar <= cantidad_personas:
          nombre.pop(indice_eliminar - 1)
          identificaciones.pop(indice_eliminar - 1)
     else:
          print('Indice fuera de rango')
elif opcion.lower() == 'v':
    valor_eliminar = input('Ingresar el valor a eliminar: ')
    if valor_eliminar in nombre:
        indice_valor = nombre.index(valor_eliminar)
        nombre.remove(valor_eliminar)
        identificaciones.pop(indice_valor)
    elif valor_eliminar in identificaciones:
        indice_valor = identificaciones.index(valor_eliminar)
        identificaciones.remove(valor_eliminar)
        nombre.pop(indice_valor)
    else:
        print('Valor no encontrado en las listas')
     

print("==============================")
print("Personas ingresadas")
print("==============================")

for i in range(len(nombre)):
    print('Mostrando los datos de la persona',i+1)
    print('Identificación:',identificaciones[i])
    print('Nombres:',nombre[i])


