'''Cuantas letras del abecedario estan en la cadena, si estan repetidas cuentela solo una vez'''
def abecedario(abc):
    list=[]
    for i in abc:
        if i not in list:
            list.append(i)
    print (len(list))  
abecedario('castillo')