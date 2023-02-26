'ZeroDivisionError'
def z_d_e(n1,n2):
    total=n1/n2
    print('El total de la division es: ',total)
try:    
    z_d_e(100,0)
except ZeroDivisionError:
    print('No se puede realizar una division por cero, esto se conoce por indeterminacion en matematicas')
except:
    print('El programa contiene otro error')
