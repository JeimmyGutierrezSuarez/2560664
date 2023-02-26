def primos():
    x=int(input('¿Que numero deseas saber si es primo o no?\n'))
    c=0
    for i in range(2,x+1):
        if x%i==0:
            c+=1
    if c>1:
        print('El numero',i,'no es primo')
    else:
        print('El numero',i,'es primo')
def perfectos():
    x=int(input('¿Que numero deseas saber si es perfecto o no?\n'))
    s=0
    for i in range(1,x):
        if (x%i) == 0:
            s+=i
    if s==x:
        print('El numero',i+1,'es perfecto')
    else:
        print('El numero',i+1,'no es perfecto')
          
def compuestos():
    x=int(input('¿Que numero deseas verificar si es numero compuesto o no?\n'))
    c=0
    for i in range(2,x+1):
        if x%2==0:
            c+=1
    if c>1:
        print('El numero',i,'es un numero compuesto')
    else:
        print('El numero',i,'no es un numero compuesto')
