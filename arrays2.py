"""
FORMA 1
nombre_de_la_lista= []

FORMA 2
otra_lista=list[]
"""
#índice     0     1     2     3
#reverse   -4   -3   -2     -1
valores = [2.5, 'Hola', True, 5.9]
#print(valores[-1])
#otra=(['Juan', 5, True, 2.9])

#Elemntos
print('Lista Original')

for valor in valores:
    print(valor)
#índices

print('Lista nuevo')
valores.append("XD")
for valor in valores:
    print(valor)
# tamaño_lista = len(valores)

#print(tamaño_lista)
# for i in range(len(valores)):
#     print(i)

# #while

# indice = 0
# while indice < len(valores):
#    print(valores[indice])
#    indice +=1 