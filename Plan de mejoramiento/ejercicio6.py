'''def funcion(a,b):
    for i in range (b):
        for j in range (a)  #Ejercicio mal ejecutado
            print(i,'-',j)
funcion(3,2)'''

        #Primer ejercicio 
def t7_70(a,b):
    for i in range(b+1):
        for p in range(a+1):
            print(i,'--',p)
t7_70(70,7)    

        #Segundo ejercicio
def input_usuario():
    a=int(input('Ingresa tu primera iteracion: '))
    b=int(input('Ingresa tu segunda iteracion: '))
    for i in range(a+1):
        for k in range(b+1):
            print(i,'---',k)
input_usuario()

        #Tercer ejercico
def usuario_100(a,b):
    for i in range(a+1):
        for k in range(b+1):
            print(i,'---',k)
a=int(input('Ingresa la unica iteracion: '))
usuario_100(a,100)