
def creandoArchivo(nombre):


    try:

        archivo=open(nombre,'w')
        archivo.write("Nombre\t")
        archivo.write("Apellido\t")
        archivo.write("Edad\t")
        archivo.write("Sexo\t")
        archivo.write("Telefono\t")
        archivo.write("Correo\n")
        print(f'Se ha creado un archivo')

    except Exception as e:
        print(f'Error al crear el archivo {e}')
    finally:
        archivo.close()

def agregarInformacio(nombreArchivo,nombre,apellido,edad,sexo,tel,email):

    try:

        archivo=open(nombreArchivo,'a',encoding='utf8')
        archivo.write(nombre)
        archivo.write(apellido)
        archivo.write(edad)
        archivo.write(sexo)
        archivo.write(tel)
        archivo.write(email)
        print(f'Se ha creado un archivo')

    except Exception as e:
        print(f'Error al crear el archivo {e}')
    finally:
        archivo.close()

def leerInformacion(nombreArchivo):
    archivo=open(nombreArchivo,'r')
    print(archivo.read())