class Conductor:        #Se crea una clase la cual es llamada Conductor
    def __init__(self,nombre,documento):    #Se crea un constructor el cual es comenzado con __init__, sus parametros son tres los cuales son self, nombre y documento
        self.__nombre=nombre        #Se crea el atributo del metodo nombre, el self llama al atributo nombre y este es igual a nombre. Este atributo es privado ya que contiene esto (.__)
        self.__documento=documento  #Se crea el atributo del metdo documento, el self llama al atributo documento y este es igual a documento. Este atributo es privado ya que contiene esto (.__)
    def getNombre(self):            #En esta linea se crea un metodo el cual es getNombre, este busca el atributo 
        return self.__nombre        #Retorna el atributo nombre
    def getDocumento(self):         #En esta linea se crea un metodo el cual es getDocumento, este busca el atributo  
        return self.__documento     #Retorna el atributo documento 
        