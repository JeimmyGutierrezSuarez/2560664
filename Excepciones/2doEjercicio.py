'IndexError'
def lista(lista,posicion):
    print(lista[posicion])
try:
    lis=[1,2,3,4,5,6]
    lista(lis,6)
except IndexError:
    print('La posicion que deseas buscar no se encuentra en la lista')
except:
    print('Tu programa ha presentado otro error')