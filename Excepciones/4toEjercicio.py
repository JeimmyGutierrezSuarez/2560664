'ValueError'
def v_e():
    x=int(input('Ingresa tu frase:\n-'))
    return x
try:
    print(v_e())
except ValueError:
    print('El programa contiene un error de valores')
except:
    print('El programa contiene un error diferente')