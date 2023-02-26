'''cuantas veces se repite un caracter dado'''
def palabra_c(frase, caracter):
    s=0
    for i in frase:
        if caracter in i:
            s+=1
    return s
usu=input('¿Qué letra quieres ver las veces que esta repetida en un texto?: ')
print(palabra_c('mi gato es hermoso, blanco y cariñoso, yo lo quiero mucho porque es muy gracioso', usu))        
    