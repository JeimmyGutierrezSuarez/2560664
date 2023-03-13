def edad(): #en esta linea define la funcion que se va a realizar en el bloque de codigo 
    try:    #Este try crea el bloque de codigo el cual verifica si hay un error en el
        tuedad=int(input("introduce tu edad"))  #en esta linea de codigo hay una varibla la cual se llama tuedad este tiene un int el cual es para ingresar numeros enteros, input sirve para que al ejecutar el codigo pueda ingresar un dato,
        #al imprimir saldra el mensaje que esta entre comillas el cual es introduce tu edad
        print(f'tu edad es  {tuedad}')  #en esta linea hay una f la cual es para llamar a la funcion tuedad entre llaves, imprime eso con un mensaje el cual es tu edad es
        #print('Tu edad es ',tuedad)
    except ValueError as e:    #en esta linea hay un except de valuError, el cual si se ingresa un valor que no es te dira que es incorrecto, as es para cambiar el ValueError por e
        print(e)    #esta linea imprime el error
        print("La edad debe ser un valor numerico...")  #esta linea imprime un mensaje el cual te dice cual fue el error cometido 
        edad()  #esta linea toma el valor el es incorrecto
    else:       #esta linea verifica si la condicion se cumple o no
        print('Viene por el else')  #si se cumple la condicion, imprime este mensaje

edad()  #esta linea llama la funcion creada 