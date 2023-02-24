values = (4, 3)     #Values es una tupla el cual contiene dos valores separados por una coma
#x,y=19,30
#print(divmod(10,3))
try:            #Este try verifica si hay un error en el bloque de codigo
    q, r = divmod(*values)      #q,r son  dos variables las cuales contienen un valor, divmod hace referencia de lo que se quiere lograr con la tupla (4,3; hacer la division entre los dos numeros)
    #print('q=',q)
    print(f'q={q}')     #imprime
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)