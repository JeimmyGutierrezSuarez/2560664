class Curso:        #En esta linea se crea la clase la cual es Curso
    def __init__(self,titulo):   #En esta linea hay un constructor ya que contiene __init__ sus parametros son self el cual siempre se debe escribir, su otro parametro es titulo.
        self.__titulo=titulo    #En esta linea esta el atributo del metodo, el self llama al atributo titulo y se le pone un igual al atributo

    def getTitulo(self):    #En esta linea se crea un metodo el cual es getNombre este busca el atributo 
        return self.__titulo       #Retorna el atributo titulo 

class Aprendiz:     #En esta linea se crea una clase la cual es Aprendiz 
    def __init__(self,nombre):  #En esta linea hay un constructor ya que contiene __init__ y su parametro es self y nombre
        self.__nombre=nombre    #Aqui se define el atributo, self llama al atributo del metodo creado el cual es nombre y se le pone se le pone el igual a nombre 
        self.__cursos=[]        #En esta linea se define una lista vacia la cual su nombre esta definido como cursos

    def agregarCurso(self,nombreCursito):   #En esta linea se crea un metodo el cual es agregarCurso y sus parametros son Self y nombreCursito
        cursito=Curso(nombreCursito)        #En esta linea se crea un objeto el cual es Cusristo y esta llama a la clase curso y hace el llamado del parametro nombrecursito 
        self.__cursos.append(cursito)   #En esta linea se define como cursos y esta agrega a la lista vacia creada anteriormente en la clase Aprendiz y se le agrega al objeto cursito

    def getCursos(self):        #En esta linea crea un metodo el cual es getCursos el cual busca el atributo
        return self.__cursos    #Retorna la lista que era vacia con sus elementos ya agregados
    
ap=Aprendiz('Sofia')        #Se crea un objeto el cual es ap este es igual a la clase Aprendiz la cual su atributo era nombre, aqui se define el nombre el cual es Sofia
ap.agregarCurso('Python Basico')    #Se crea un objeto el cual es ap y llama a la clase creada agregarCurso en este se define el atributo el cual es Python Basico
ap.agregarCurso('Python Intermedio')    #Se crea un objeto el cual es ap y llama a la clase creada agregarCurso en este se define el atributo el cual es Python Basico

for c in ap.getCursos():        #En esta linea se crea un ciclo for el cual recorre el objeto ap el cual es aprendiz, con el metodo getCursos
    print(c.getTitulo())        #En esta linea imprime lo que encontro en la lista getTitulo
