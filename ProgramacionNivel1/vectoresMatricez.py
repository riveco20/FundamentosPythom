def crearVectores():
    import numpy as np
    opcion=None
    elementos=list()
    while opcion!=0:
        vector = np.array(elementos)
        cantidad=None
        try:
            print(f'operacion'.center(50, '-'))
            print('1. crear vector')
            print('2. Mostrar vector')
            print('3. Eliminar vector')
            print('0. Salir')
            opcion=int(input('Selecione una opcion: '))
            if opcion==1:
                print('Agregando elementos'.center(50,'-'))
                cantidad=int(input('Cuantos elementos desea agregar: '))
                print('Ingrese los numeros')
                contador=0
                while contador<cantidad:
                    elemento=int(input(':'))
                    if elemento>20 and elemento<50:
                        elementos.append(elemento)
                        contador+=1
                    else:
                        print('El rango de los elementos es entre 20 - 50 ')
                        contador+=0
                else:
                    print(f'Vector creado {elementos}')
            elif opcion==2:
                print('Vector'.center(5,'-'))
                print(vector)
            elif opcion==3:
                limite=vector.size
                print(limite)
                nuevoVector=np.delete(vector,(0,limite-1))
                vector=np.array(nuevoVector)
                print(vector)
                print('Vector eliminado')
        except Exception as e:
            print(f'Ocurrio un error {e}')
            opcion=None
    else:
        print('Salio del programa')