

def AgregarInformacio(informacion):
    nombre=input('Ingrese su nombre: ')
    apellido=input('Ingrese su apellido: ')
    edad=input('Ingrese su edad: ')
    telefono=input('Ingrese su numero de telefono: ')
    direccion=input('Su direccion: ')
    informacion['nombre   : ']=nombre
    informacion['Apellido : ']=apellido
    informacion['Edad     : ']=edad
    informacion['Telefono : ']=telefono
    informacion['Direccion: ']=direccion
    print('Se agrefado la informacion')
def informacion():
    informacion=dict()
    opcion=None
    while opcion!=0:
        try:
            print('Que quieres hacer'.center(50,'-'))
            print('1. Ingresar datos')
            print('2. Ver informacion')
            print('3. Eliminar informacio')
            print('0. Salir')
            opcion=int(input('Elija la opcion: '))
            if opcion==1:
                print('Argregar informacion'.center(50,'-'))
                AgregarInformacio(informacion)

            elif opcion==2:
                print('Mostrar informacion'.center(50,'-'))
                for clave,valor in informacion.items():
                    print( clave,valor)
            elif opcion==3:
                del informacion['Edad     : ']
                print('Informacion eliminada'.center(50, '-'))
                for clave, valor in informacion.items():
                    print(clave, valor)

            else:
                if opcion>3:
                    print('La opcion esta fuera de rango')

        except Exception as e:
            print(f'Ocurrio un error {e}')
    else:
        print('Gracias hasta pronto')