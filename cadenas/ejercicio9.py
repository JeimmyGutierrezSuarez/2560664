'''Imprima todas las subcadenas que salen de una cadena comenzando con las dos primeras letras, luego tres primeras y así sucesivamente hasta llegar a la última'''
def impresion(cadena):
      ci=1
      for i in cadena:
        ci+=1
        print(cadena [0:ci])
usu=input('Digita tu frase: ')
impresion(usu)   