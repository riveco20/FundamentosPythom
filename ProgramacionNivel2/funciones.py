#Este acrhivo permite crear funciones



'''def factorial(numero):
    num=numero

    if num>0:
        calculo=1
        resultado=None
        for i in range(1,numero+1,1):
            calculo*=i

        resultado=calculo
        print(f'Resultado del factorial {resultado}')
    else:
        print('Proporcione un numero positivo')
'''
'''def funcionOr(bytes1,bytes2,resultado1):
       for i, j in zip(bytes1, bytes2):
            if i == "1" and j == "1":
                a = "1"
                resultado1.append(a)
            elif i == "0" and j == "0":
                a = "0"
                resultado1.append(a)
            else:
                a = "1"
                resultado1.append(a)
def funcionAnd(bytes1,bytes2,resultado1):
    for i, j in zip(bytes1, bytes2):
        if i == "1" and j == "1":
            a = "1"
            resultado1.append(a)
        elif i == "0" and j == "0":
            a = "0"
            resultado1.append(a)
        else:
            a = "0"
            resultado1.append(a)
def funcionXor(bytes1,bytes2,resultado1):
    for i, j in zip(bytes1, bytes2):
        if i == "1" and j == "1":
            a = "0"
            resultado1.append(a)
        elif i == "0" and j == "0":
            a = "0"
            resultado1.append(a)
        else:
            a = "1"
            resultado1.append(a)


def cacluladora(bytes1,bytes2,op):
    resultado1=list()
    if len(bytes1)==len(bytes2):
        if op=="OR":
            funcionOr(bytes1,bytes2,resultado1)
        elif op=="AND":
            funcionAnd(bytes1,bytes2,resultado1)
        else:
            funcionXor(bytes1,bytes2,resultado1)
    else:
        print("Las cadenas deben tener el mismo tamaño")
    resultado=''.join(map(str, resultado1))
    return resultado

var1= cacluladora( "0110110110","1100011101","AND")
print(var1)'''#Reto 3
'''def totalFactura(precio):
    precio=precio
    iva=precio*0.21
    pagar=precio+iva
    print(f'Total a pagar: {pagar}')'''