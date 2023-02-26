'''El siguiente programa evaluara el numero ingresado
por el usuario y dira si es de una cifra, dos cifras, tres cifras 
o cuatro cifras, esto quiere decir que si el numero es mayor o
igual a 10000 o si es menor a 0 entonces aparecera el error assert
creado por mi'''
def cifras(n1):
    assert n1>0,'Los menores a 0 son negativos por esto no cuentan'
    assert n1<10000,'Los numeros despues de 10000 son de cinco cifras'
    if n1 <=9:
        print("El numero es de 1 cifra")
    elif n1 <=99:
        print("El numero es de 2 cifras")    
    elif n1 <=999:
        print("El numero es de 3 cifras")
    elif n1<=9999:
        print("El numero es de 4 cifras")
cifras(100001) 