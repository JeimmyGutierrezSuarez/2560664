from Vehiculo import *      #De carga importa todo,from quiere decir que busca el archivo Vehiculo, import este importa todo lo que esta en el archivo Vehiculo
class Carga(Vehiculo):      #Esta es una clase la cual es Carga y tiene como herencia Vehiculo que es la clase padre
    def __init__(self,placa,conductor,capacidad,ejes):    #En esta linea hay un constructor ya que contiene __init__ sus parametros son self el cual siempre se debe escribir, sus otros parametros son placa, conductor, capacidad y ejes.
        Vehiculo.__init__(self,placa,conductor)     #En esta linea llama al contructor de la clase padre y sus parametros son, self, placa y conductor.
        self.__capacidad=capacidad      #En esta linea esta el atributo del metodo carga, el self llama al atributo capacidad y se le pone un igual al atributo. Este atributo es privado ya que contiene esto (.__).
        self.__ejes=ejes    #En esta linea esta el atributo del metodo carga, el self llama al atributo ejes y se le pone un igual al atributo. Este atributo es privado ya que contiene esto (.__).
    def getCapacidad(self):     #Se crea un  metodo el cual es getCapacidad y este  busca el atributo creado
        return self.__capacidad     #Este retorna al atributo capacidad  
    def getEjes(self):      #Se crea un  metodo el cual es getejes y este  busca el atributo creado
        return self.__ejes      #Este retorna al atributo ejes