'FileNotFoundError'
def file():
    try:
        x=open('fichero.txt')
        print(x)
    except FileNotFoundError:
        print('El archivo buscado no pudo ser encontrado')
    except:
        print('El programa sufre de otro error')
    else:
        print(x.read())
file()