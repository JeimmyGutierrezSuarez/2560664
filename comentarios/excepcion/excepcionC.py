def try_syntax(numerator, denominator): #En esta linea de codigo se define la funcion que va a tener el codigo, el cual es numerador y denominador son dos funciones diferentes 
    try:  #Este try crea el bloque de codigo el cual verifica si hay un error en el
        print(f'In the try block: {numerator}/{denominator}')   #imprime un mensaje con el valor que le dieron a la funcion numerados y denominador, esta linea de codigo lleva una f para despues concatenar numerador y denominador, en este lleva un slash (/) que hace referencia una division, para hacer la division entre los dos numeros  
        result = numerator / denominator    #en esta linea define el resultado del numerador y denominador haciendo la division entre ellos
    except ZeroDivisionError as ppp:    #en esta linea hay un except el cual menciona el tipo de error (ZeroDivisionError) hay un as y al lado una variable la cual replaza el nombre de ZeroDivision 
        print(ppp)      #esta linea de codigo imprime si ese excepet se cumple con el numero 0 
    else:       #esta linea verifica si la condicion se cumple o no 
        print('The result is:', result)     #si se cumple imprime esta linea de codigo el cual es un mensaje que es, el resultado es (este va entre comillas para que al imprimir se muestre en pantalla) va unacoma(,) para concatenarlo con la linea creada cuatro del bloque de codigo el cual muestra el resultado de la division
        return result       #esta linea retorna el resultado dado de la division del umerador y denominador
    finally:    #finaliza el bolque try
        print('Exiting')    #esta linea imprime existe
        #return "Fallo por zero"
#print(try_syntax(12, 4))
print(try_syntax(11,3 ))    #esta linea llama con el nombre que le dio la funcion y llena sus dos parametros los cuales son numerador y denominador  