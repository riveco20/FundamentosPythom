#lista materia

def agregarMateria(materias):
    print('Agregar materia'.center(50,'-'))
    materia=input('Ingrese la materia: ')
    if materia in materias:
        print('La materia ya existe')
    else:
        materias.add(materia)
        print(f'Agregar la materia {materia}')
def eliminarMateria(materias):
    print('Eliminar materia'.center(50,'-'))
    eliminar=input('Nombre de la materia a eliminar: ')
    if eliminar in materias:
        materias.remove(eliminar)
        print(f'Materia eliminada correctamente {eliminar}')
    else:
        print('La materia no existe')

def mostrarMaterias(materias):
    print('Lista materias'.center(50,'-'))
    contador=0;
    conte=len(materias)
    if conte>0:
        for i in materias:
            contador += 1
            print(contador, ':', i)
    else:
        print('La lista esta vacia')

def materias():
    materias=set()
    opcion=None
    while opcion!=0:
        try:
               print('Que quieres hacer'.center(50,'-'))
               print('1. Agregar materia')
               print('2. Eliminar materia')
               print('3. Mostrar materia')
               print('0 salir')
               opcion=int(input('Elija una opcion: '))
               if opcion==1:
                   agregarMateria(materias)
               elif opcion==2:
                   eliminarMateria(materias)
               elif opcion==3:
                   mostrarMaterias(materias)
               else:
                   if opcion>4:
                       print('Fuera de rango')
        except Exception as e:
            print('Ocurrio un error, Ingrese un numero no una letra')
    else:
        print('Salio del programa')
