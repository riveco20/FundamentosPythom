def listaMateria():
    opcion=None
    materias=list()
    while opcion!=0:
        try:
            print('Selecione una opcion'.center(50,'-'))
            print('1. Agregar material')
            print('2. Eliminar elemento de una lista')
            print('3. Mostrar lista')
            print('0. Salir')
            opcion=int(input('Seleccione una opcion: '))
            if opcion==1:
                materia=input('Ingrese el nombre de la materia: ')
                materias.append(materia)
            elif opcion == 2:
                i = int(input('El indice de la material que quieres eliminar: '))
                materias.pop(i)
            elif opcion==3:
                print('Lista Materias'.center(50,'-'))
                for i in materias:
                    print(i)
            else:
                if opcion>4:
                    print('El valor esta fuera del rango')
        except Exception as e:
            print(f'ocurrrio un error{e}')
    else:
        print('Salio del programa')
