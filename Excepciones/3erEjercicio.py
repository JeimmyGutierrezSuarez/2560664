'TypeError'
def s_e(palabra1,palabra2):
    suma=palabra1+palabra2
    print('El total de la suma es:',suma)
try:
    s_e('10',15)
except TypeError:
    print('Existe un error de tipos de dato no coherentes')
except:
    print('El programa presenta otro problema')