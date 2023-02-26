'NameError'
def s_error(string):
    pri(string)
try:
    s_error('Hola')
except NameError:
    print('Alguna de las variables no esta definida')
except:
    print('Tu programa presenta otro error')