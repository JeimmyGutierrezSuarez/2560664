'''Pida un numero al usuario que representa días del año. Diga a que mes del año
corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días.'''

usuario=int(input('Ingresa un numero para ver a que mes corresponde del año: '))
if usuario<31:
    print('El mes corresponde a enero')
elif usuario<59:
    print('El mes corresponde a Febrero')
elif usuario<90:
    print('El mes corresponde a marzo')
elif usuario<118:
   print('El mes corresponde a abril')
elif usuario<149:
    print('El mes corresponde a mayo')
elif usuario<179:
    print('El mes corresponde a Junio')
elif usuario<210:
    print('El mes corresponde a Julio')
elif usuario<241:
    print('El mes corrsponde a Agosto')
elif usuario<271:
   print('El mes correesponde a Septiembre')
elif usuario<302:
    print('El mes corresponde a Octubre')
elif usuario<332:
    print('El mes corresponde a Noviembre')
elif usuario<363:
    print('El mes corresponde a Diciembre')