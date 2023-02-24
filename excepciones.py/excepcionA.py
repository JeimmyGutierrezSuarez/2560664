#Este try verificara si hay una falla de sintaxis
try:        #Creación deel bloque de excepcion
    #print(1/1))        
    raise SyntaxError       #Raise hace que haya un error al tiempo de escribir
except SyntaxError:         #este except dira el tipo de error comedido el cual es SyntaxError
    print('Cierra el parentesis')      #muestra el error que has comedito atra ves de un print 