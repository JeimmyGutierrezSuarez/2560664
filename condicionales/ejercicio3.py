'''Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número 
exceda los límites emita un mensaje y finalice el programa'''
l=int(input('Ingresa numeros no mayor a cinco cifras: '))
if l<9:
    print('El numero es de una cifra')
elif l<99:
    print('El numero es de dos cifrras') 
elif l<999:
    print('El numero es de tres cifras')
elif l<9999:
    print('El numero es de cuatro cifras')
elif l>9999:
    print('¡ERROR!')

    