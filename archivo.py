#file = open('data.txt', 'r')
#print(file)
#lineas = file.readlines()
#print(lineas)
#file.close()

#with open ('data.txt','r') as file:
#    lineas=file.readlines()
#    print(lineas)
#
#for line in lineas: 
#    print(line.replace('\n',''))
#Escritura----------------

with open ('data2.txt','w') as file:
    file.write("Todas mienten")
    print("Archivo creado correctamente")

#Modifica--------------------------------
with open ('data2.txt','a') as file:
    file.write("Todas mienten")
    print("Archivo creado correctamente")