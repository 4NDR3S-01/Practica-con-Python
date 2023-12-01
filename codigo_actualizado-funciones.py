productos = [(15, "Cepillo", 25.6), (2, "Crema dental", 2.75)]

def VerificarContrasena(contrasena):
    # 10 caracteres
    # Mayusculas al menos una
    # Al menos un numero
    if len(contrasena) >= 10 and any(char.isupper() for char in contrasena) and any(char.isdigit() for char in contrasena):
        return True
    else:
        return False

def CalcularIva(valor):
    iva = valor * 0.12
    return iva

def MostrarProductos():
    print("Lista de productos:")
    for producto in productos:
        print(producto)

def AgregarProductos(id, nombre, precio):
    for producto in productos:
        if producto[0] == id:
            print(f"El ID {id} ya existe y no se puede agregar el producto.")
            return
    productos.append((id, nombre, precio))
    print("Producto agregado correctamente.")
    print("Lista de productos actualizada:")
    MostrarProductos()

menu = """
Escoja una opcion del menu
1. Agregar Producto
2. Calcular Iva
3. Verificar Contraseña
4. Salir
"""

requisitodecontrasena = """
Mas de 10 caracteres
Al menos una mayuscula
Al menos un numero
"""

while True:
    print(menu)
    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
            MostrarProductos()
            respuesta = input("¿Desea ingresar un nuevo producto? (si/no): ")
            if respuesta.lower() == 'si':
                id_producto = int(input("Ingrese el ID del producto: "))
                nombre_producto = input("Ingrese el nombre del producto: ")
                precio_producto = float(input("Ingrese el precio del producto: "))
                AgregarProductos(id_producto, nombre_producto, precio_producto)
            elif respuesta.lower() == 'no':
                continue
            else:
                print("Opción no válida. Regresando al menú principal.")

    elif opcion == "2":
        MostrarProductos()
        seleccionproducto = int(input("Ingrese el ID del producto para calcular el IVA: "))
        producto_seleccionado = next((producto for producto in productos if producto[0] == seleccionproducto), None)
        if producto_seleccionado:
            precio_producto_seleccionado = producto_seleccionado[2]
            iva_calculado = CalcularIva(precio_producto_seleccionado)
            print(f"El IVA calculado para el producto seleccionado es: {iva_calculado}")
        else:
            print(f"No se encontró un producto con el ID {seleccionproducto}.")

    elif opcion == "3":
        while True:
            contrasena = input("Ingrese la contraseña a verificar: ")
            if VerificarContrasena(contrasena):
                print("Contraseña válida.")
                break
            else:
                print("Contraseña inválida, la contraseña debe contener:")
                print(requisitodecontrasena)

    elif opcion == "4":
        print("Saliendo del programa.....")
        break

    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")