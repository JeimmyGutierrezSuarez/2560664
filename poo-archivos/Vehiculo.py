class Vehiculo:     #Se crea una clase la cual es Vehiculo
    def __init__(self,placa,conductor):     #En esta linea se crea un constructor ya que comienza con __init__, contiene tres parametros los cuales son self, placa y conductor 
        self.__placa=placa      #Se crea el atributo del metodo placa, el self llama al atributo placa y este es igual a placa. Este atributo es privado ya que contiene esto (.__)
        self.__conductor=conductor      #Se crea el atributo del metodo conductor, el self llama al atributo conductor y este es iguañ a conductor. Este atributo es privado ya que contiene esto (.__) 
    def getConductor(self):     #Se crea un  metodo el cual es getConductor y este  busca el atributo creado
        return self.__conductor     #Este retorna el atributo conductor
    def getPlaca(self):     #Se crea un metodo el cual es getPlaca y este bsuca el atributo creado
        return self.__placa     #Este retorna el atributo placa