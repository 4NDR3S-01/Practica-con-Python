import os
import tempfile

#Definir una funcion paro implementar el metodo nameditempfile
def example_named_temp_file():
    try:
        #Uso de la NamedTemporaryFile
        with tempfile.NamedTemporaryFile(mode="w+", delete=True) as temp_file:
            temp_file.write("Hola, este es un ejemplo de fichero temporal en python\n")
            temp_file.write("Puedes agregar mas contenido...\n")
            temp_file.seek(0)#Mover el puntero al principio del fichero

            #Leer y mostrar el contenidl del ficheoro
            print("Mostrar el contenido del fichero\n")
            print(temp_file.read())
        #el dichero se elimina automaticamente al salir del bucle
    except Exception as e:
        print(f"Error: {e}")

def exampl_mkstemp():
    try:
        temp_fd, temp_name=tempfile.mkstemp()
        with os.fdopen(temp_fd, "w+") as temp_file:
            #Escribir datos en el fichero
            temp_file.write("Este es el ejemplo utilizando mkstemp \n")
            temp_file.write("Aqui puedes agregar mas contenido")
            temp_file.seek(0)#Mover el puntero al principio del fichero

            print("Los datos del segundo fichero con mkstemp son: \n")
            print(temp_file.read())
        #el dichero se elimina automaticamente al salir del bucle
    except Exception as e:
        print(f"Error: {e}")

    
example_named_temp_file()
exampl_mkstemp()
