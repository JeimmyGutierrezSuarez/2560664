class Conductor:        #Se crea una clase la cual es llamada Conductor
    def __init__(self,nombre,documento):    #Se crea un constructor el cual es comenzado con __init__, sus parametros son tres los cuales son self, nombre y documento
        self.__nombre=nombre    #Se crea el atributo del metodo nombre y este es igual a nombre
        self.__documento=documento      #Se crea el atributo del metdo documento y este es igual a documento 
    def getNombre(self):            #
        return self.__nombre
    def getDocumento(self):
        return self.__documento
        