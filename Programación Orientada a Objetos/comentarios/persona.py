class Persona:   #En esta linea se define la clase la cual es Persona
    def __init__(self,nombre): #En esta linea define la función, _init__ es utilizado para iniciar la clase creada, los parametros son self el cual es para acceder a los atributos, el parametro nombre es para definir el nombre de clase persona
        self.__nombre=nombre    #Self define un atributo del metodo __init__ el cual toma el parametro nombre, este sera igual a nombre
        print('Activando constructor')  #Se imprime cada vez que hay un objeto creado para la clase Persona

    '''def ahora es un metodo y siempre deben terner el parametro self. (Self.) son atributos del metodo'''
    def getNombre(self):    #En esta linea se crea un metodo el cual es getNombre este busca el atributo .Nombre que fue creado anteriormente el self identifica que esta dentro de la clase persona
        return self.__nombre    #En esta linea retorna el atributo que fue creado dentro del constructor de la clase persona 
    
        #set modifica 
    def setNombre(self, nombre):     #En esta linea se crea un metodo el cual es setNombre, este modifica el atributo getNombre el self identifica que esta dentro de la clase persona, el parametro nombre define el nombre por el cual va a ser cambiado
        self.__nombre=nombre    #Self define el atributo por el cual va hacer cambiado 

    def metodo(self):   #En esta linea se define un metodo
        print('Soy un método') #Imprime si es un metodo


ob=Persona('Ana')   #ob es un objeto la cual es de la clase persona la cual su parametro (nombre) es Ana
print(ob.getNombre())   #imprime el objeto que llama el metodo getNombre el cual es su parametro Ana   
ob.setNombre('Maria')   #Esta linea modifica el metodo getNombre por el parametro que era Ana por el metodo setNombre para que el parametro cambie a Maria 
print(ob.getNombre())   #Imprime Maria ya que getNombre fue remplazado por setNombre
 