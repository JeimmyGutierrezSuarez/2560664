''' def funcion(dictionary,key,value):
if key not in dictionary.keys():
    dictionary[key] = value
    print('dictionary')
else:                                                  #Ejecicio mal ejecutado
    print('Existe')
di={"gato":"cat","perro":"dog","caballo":"horse"}
funcion(di,'perro','rabbit')'''

        #Primer ejercicio
def datos_personales():
    usuario={'nombre':[],
    'apellido':[],
    'edad':[],
    'numero_cel':[]}

    q=input('¿Quieres ingresar tus datos personales ("si"/"no")? ')
    print('Decidiste no ingresar datos, muchas gracias por participar')
    while q!='no':
        a=input('Ingresa tu nombre: ')
        b=input('Ingresa tu apellido: ')
        c=int(input('Ingresa tu edad: '))
        d=int(input('Ingresa tu numero de celular: '))
        v=input('¿Quieres continuar el ciclo? si/no ')
        if a == usuario ['nombre']:
            print('El nombre ya existe')
        if a != usuario ['nombre']: 
            usuario['nombre'].append(a)
        if b == usuario['apellido']:
            print('El apellido ya existe')
        if b != usuario ['apellido']:
            usuario['apellido'].append(b)
        if c == usuario['edad']:
            print('La edad ya existe en el diccionario')
        if c != usuario['edad']:
            usuario['edad'].append(c)
        if d == usuario['numero_cel']:
            print('El numero de telefono ya existe en el diccionario')
        if d != usuario['numero_cel']:
            usuario['numero_cel'].append(d)
        if v =='si':
            print('!Sigue ingresando tus datos personales¡')
            continue
        if v == 'no':
            print('Los datos personales que ingresaste son')
            break
    print(usuario)
datos_personales()

        #Segundo ejercicio
def par_impar():
    numeros={'Pares':[],
            'impares':[]}
    while True:
        a=int(input('ingresa los numeros que desees o pulsa "0" para salir o no empezar '))
        if a > 0:
            numeros['Pares'].append(a)
        if a < 0:
            numeros['impares'].append(a)
        if a == 0:
            break
    print('Los numeros que ingresaste ordenados por pares e impares son: ')
    print(numeros)
par_impar()

        #Tercer ejercicio
def operaciones():
    operaciones={}
    print('Haremos operaciones con diferentes numeros, primero iniciaremos con la suma, resta, multplicacion y division')
    suma1=int(input('Ingresa el primer numero para la suma: '))
    suma2=int(input('Ingresa el segundo numero para la suma: '))
    totalsuma=suma1+suma2
    resta1=int(input('Ingresa el primer numero para la resta: '))
    resta2=int(input('Ingresa el segundo numero para la resta: '))
    totalresta=resta1-resta2
    multiplicacion1=int(input('Ingresa el primer numero para la multiplicacion: '))
    multiplicacion2=int(input('Ingresa el segundo numero para la multiplicacion: '))
    totalmultiplicacion:multiplicacion1*multiplicacion2
    division1=int(input('Ingresa el primer numero para la division: '))
    division2=int(input('Ingresa el segundo numero para la division: '))
    totaldivision=division1//division2
    operaciones.update({'Suma':totalsuma,
                        'Resta':totalresta,
                        'Multiplicacion':totalmultiplicacion,
                        'Division':totaldivision})
    print(f'El resultado total de todas las operaciones es {operaciones}')
operaciones()