#Funcion es una porcion de codigo que realiza una accion especifica
#Funcion que no recibe parametros
#def Saludo():
#    print("Hola clase")

#Saludo()

#def Saludo(Nombre, carrera, nivel=2):
#    print("Hola clase", Nombre ," de la carrera de ", carrera, "Nivel ", nivel)
#clase=input("Ingrese el nombre de la clase: ")    
#carrera=input("Ingrese el nombre de la carrera: ")
#nivel=input("Ingrese el nivel: ")
#Saludo(carrera=carrera, Nombre=clase)

#def Sumar(a,b):
    # print(a+b)
#    return a + b
    #print("Despues del return")

#a = int(input("Ingrrese el valor 1: "))
#b = int(input("Ingrrese el valor 2: "))

#Resultado = Sumar(a,b)
#print(Resultado)



#variables va a cambiar
#externa="Externa" #La vida de esta variable dura mientras se ejecute el programa

#def cualquiera(interna="interna"):
#    print(interna) #Solamente va a existir mientras se ejecute y cuando se ejecute dentro del progrma
#cualquiera()
#print(externa, interna)

productos=[(15, "Cepillo", 25.6), (2,"Crema dental", 2.75)]

def VerificarContrasena(contrasena):
    #10 caracteres
    #Mayusculas al menos una
    #Almenos un numero
    if len(contrasena) >= 10 and any(char.isupper() for char in contrasena) and any(char.isdigit() for char in contrasena):
        return True
    else:
        return False

def CalcularIva(valor):
    iva = valor * 0.12
    return iva

def AgregarProductos(id, nombre, precio):    
    for producto in productos:
        if producto[0] == id:
            print(f"El ID {id} ya existe y no se puede agregar el producto.")
    else:
        productos.append((id, nombre, precio))
        print("Producto agregado correctamente.")
        print("Lista de productos actualizada:")
        for producto in productos:
            print(producto)

menu="""
Escoja una opcion del menu
1. Agregar Producto
2. Calcular Iva
3. Verificar Contraseña
4. Salir
"""

requisitodecontrasena="""
Mas de 10 caracteres
Al menos una mayuscula
Al menos un numero
"""

while True:
    print(menu)
    opcion = int(input("Ingrese el número de la opción deseada: "))

    if opcion == 1:
        id_producto = int(input("Ingrese el ID del producto: "))
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        AgregarProductos(id_producto, nombre_producto, precio_producto)

    elif opcion == 2:
        print(productos)
        seleccionproducto = int(input("Ingrese el id del producto: "))
        if seleccionproducto == productos:
            print(f"El IVA calculado es: {iva_calculado}")

    elif opcion == 3:
         while True:
            contrasena = input("Ingrese la contraseña a verificar: ")
            if VerificarContrasena(contrasena):
                print("Contraseña válida.")
                break
            else:
                print("Contraseña inválida, la contraseña debe contener:")
                print(requisitodecontrasena)

    elif opcion == 4:
        print("Saliendo del programa.....")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")