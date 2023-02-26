'''De una cadena diga cuantas vocales tiene, cuantas consonantes, cuantas vocales con tilde y cuantos caracteres especiales.''' 
def verificar(palabra):
    ra=0
    rs=0
    rd=0
    rf=0
    a='BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz'
    s='AEIOUaeiou'
    d='ÁÉÍÓÚRáéíóú'
    f='!¡?¿+*-_.," '
    for i in palabra:
        if i in a:
            ra+=1
            #print('En la palabra ingresada hay', ra,'consonantes')
        elif i in s:
            rs+=1
            #print('En la palabra ingresada hay', rs, 'vocales')
        elif i in d:
            rd+=1
           # print('En la palabra ingresada hay', rd, 'vocales con tilde')
        elif i in f:
            rf+=1
    print('En la palsbra ingresada hay', rf, 'de caractes especiales')     
    print('En la palabra ingresada hay', ra,'consonantes')   
    print('En la palabra ingresada hay', rs, 'vocales') 
    print('En la palabra ingresada hay', rd, 'vocales con tilde')
usu=input('Digita alguna frase: ')
verificar(usu)

