'''Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
valor del medio es 11. No use operadores lógicos'''

a=int(input('Ingresa el primer numero: '))
b=int(input('Ingresa el segundo numero: '))
c=int(input('Ingrsa el tercer numero: '))

if a>b:
    if a<c:
        print('El numero de el medio es',a)
if a<b:
    if a>c:
        print('El numero del medio es', a)
if b<a:
    if b>c:
        print('El numero del medio es',b)
if b>a:
    if b<c:
        print('El numero del medio es',b)
if c<a:
    if c>b:
        print('El numero del medio es',c)
if c>a:
    if c<b:
        print('El numero del medio es',c)







  









