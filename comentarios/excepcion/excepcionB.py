values = (10,2)     #Values es una tupla el cual contiene dos valores separados por una coma10
#x,y=19,30
#print(divmod(10,3))
try:            #Este try crea el bloque de codigo el cual verifica si hay un error en el
    q, r = divmod(*values)      #q,r son  dos variables las cuales contienen un valor, divmod hace referencia de lo que se quiere lograr con la tupla (10,2; hacer la division entre los dos numeros)
    #print('q=',q)
    print(f'q={q}')     #imprime el resultado que da el dividiendo (10) con la letra (q), este print lleva f el cual se usa para concaternarlo con corchetes en ves de una coma 
    print(f'r={r}')     ##imprime el resultado que da el divisor (2) con la letra (r), este print lleva f el cual se usa para concaternarlo con corchetes en ves de una coma
except (ZeroDivisionError, TypeError) as e: #En este codigo se encuentran dos excepciones en la misma linea concatenadas  por una coma (,) para hacer la diferenciación entre estas dos diferentes excepciones 
    #hay un as y al lado una variable la cual replaza el nombre de ZeroDivisonError y TypeError                     
    print(type(e), e)      #esta linea imprime el tipo de error lo llaman con la letra que le fue asignada la cual es la e y va entre parentesis, cada una toma el tipo de error para imprimir el inidcado   