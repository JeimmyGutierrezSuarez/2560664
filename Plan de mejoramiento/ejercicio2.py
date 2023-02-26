'''def funcion(num)
    while num>0:
        if num%2==0       #ejercicio incorrecto
            print(num)
        num-=1
    funcion(12)'''


        #Primer ejercicio
def validacion (email):
    direccion='@'
    i = 0
    while i < len (email):
        if email [i] == direccion:
            return True
        i+=1
email=input('Ingresa tu email: ')
if validacion (email):
    print('Dirección valida')
else: 
        print('Dirección invalida, intenta de nuevo')

        #Segundo ejercicio
def validacion ():
    usuario= input('digite su contraseña: ')
    usuario1= input('Vuelve a confirmar la contraseña: ')
    intentos= 3
    i=0
    if usuario == usuario1:
        print('La contraseña es correcta')
    while usuario != usuario1 :
        print('¡Contraseñas incorrectas! intente de nuevo')
        i+=1
        usuario11= input('Vuelva a confirmar la contraseña: ')
        
        if usuario == usuario11:
            print('¡Contraseña correcta!')
            break
        if i == intentos:
            print('Has superado el numero de intentos')
            break 
validacion()

        #Tercer ejercicio
def funcion ():
    i=0
    while i<10:
        i+=1
        if i == 7:
            continue
        print(i)
funcion()


