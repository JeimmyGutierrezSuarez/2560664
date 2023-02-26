'''Escribe un programa que pida tres números y que escriba si son los tres 
iguales, si hay dos iguales o si son los tres distintos'''
a=int(input('Ingresa el primer numero: '))
s=int(input('Ingresa un segundo numero: '))
d=int(input('Ingresa un tercer numero: '))
if a!=s!=d:
    print('Los tres numeros ingresados son diferentes')
if a==s==d:
    print('Los tres numeros ingresados son iguales')
if a==s:
    print(f'los numeros {a} y {s} son iguales')
if d==a:
    print(f'Los numeros {d} y {a} son iguales')
if s==d:
    print(f'Los numeros {s} y {d} son iguales')

