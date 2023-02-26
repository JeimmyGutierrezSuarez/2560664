'''
a=4
b=3
c=5                  #Ejercicio malito
rta=c//b+a*a-b+c
print(rta)
'''
        #Primer ejercicio
def una_vez(a):
    b=12
    c=40
    resultado= c//b+a*a-b+c*a-c+b//c
    print('El resultado de la operacion con el numero ingresado y b= 12 y c= 40 es igual a: ',resultado)
a=int(input('Ingresa la variable para la operacion: '))
una_vez(a)

        #Segundo ejercicio
def me(a,b,c,d,e):
    respuesta=a+c*d//b-e+a-c
    print(f'El resultado de la operacion es {respuesta}')
me(15,22,55,32,9)

        #Tercer ejercicio
def sumando_(a,b,c):
    suma=a+b+c
    resta=a-b-c
    multiplicacion=a*b*c
    division=a//b//c
    print(f'El resultado de esta operacion es {suma+resta+multiplicacion+division}')
a=int(input('Ingresa el primer numero: '))
b=int(input('Ingresa el segundo numero: '))
c=int(input('Ingresa el tercer numero: ' ))
sumando_(a,b,c)
