'''def funcion (a,b):
    if a>b:
        print('descendente') ejercicio mal 
    elif a<b:
        print('ascendente')
    else:
        print('iguales')
a=1/5
b=1/4
funcion(a,b)'''
        #Primer ejercicio
def funcion ():
    año_actual=int(input('¿En que año esta?: '))
    año_diferente=int(input('Digite cualquier año: '))
    if año_actual < año_diferente:
        print(f'Faltan {año_diferente - año_actual} años para el año {año_diferente}')
    elif año_actual > año_diferente:
        print(f'Han pasado {año_actual- año_diferente} años desde {año_diferente}')
    else:
        print('Estas en el mismo año')
funcion()

        #Segundo ejercicio
def funcion ():
    niño1=input('Ingresa tu nombre: ')
    niño11=int(input('Ingresa tu edad: '))
    niño2=input('Ingresa tu nombre: ')
    niño22=int(input('Ingrsa tu edad: '))
    if niño11 > niño22:
        print(f'El niño {niño1} tiene {niño11} y es mayor que el niño {niño2} que tiene {niño22} ')
    elif niño11 < niño22:
        print((f'El niño {niño1} tiene {niño11} y es menor que el niño {niño2} que tiene {niño22} '))
    elif  niño22 > niño11:
        print(f'El niño {niño2} tiene {niño22} y es mayor que el niño {niño1} que tiene {niño11} ')
    elif niño22 < niño11:
        print((f'El niño {niño1} tiene {niño11} y es menor que el niño {niño2} que tiene {niño22} '))
    else:
        print(f'El niño {niño1} de {niño11} y {niño2} de {niño22} tienen la misma edad')
funcion()
        #Tercer ejercicio
def funcion ():
    dia=30
    mes=12
    año=2060
    usuariodia=int(input('Digite un dia: '))
    usuariomes=int(input('Digite el mes: '))
    usuarioaño=int(input('Digita año: '))
    if usuariodia > dia or usuariomes > mes or usuarioaño > año:
        print(f'El día {usuariodia} del mes {usuariomes} del año {usuarioaño} no existe')
    else: 
        print(f'El día {usuariodia} del mes {usuariomes} del año {usuarioaño} existe')
funcion()
    