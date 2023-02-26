'''def funcion (a,b,c):
    for i in range (a,b,c):        #Ejercico mal ejecutado
        print(i)
funcion(50,0,-5)'''


        #Primer ejercicio
def aumento5_5():
    usuario=int(input('Digita un numero para iniciar: '))
    usuario2=int(input('Digita un numero para finalizar: '))
    for i in range (usuario,usuario2+5,5):
        print(i)
aumento5_5()

 
        #Segundo ejercicio
def retrocediendo():
    usuario1=int(input('Digita un numero: '))
    usuario2=int(input('Digita un numero para finalizar: '))
    if usuario1 > usuario2:    
        for i in range (usuario1,usuario2-1,-1):
            print(i)
retrocediendo()


        #Tercer ejercicio
def aumentando100_100(a,b,c):
    for i in range (a,b,c):
        print(i)
aumentando100_100(1,10000+1,99)