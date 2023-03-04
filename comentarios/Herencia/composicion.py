class Aprendiz:         #En esta linea se crea una clase la cual es Aprendiz 
    def __init__(self,nombre):      #En esta linea se crea un constructor el cual tiene como atributo self y nombre
        self.__nombre=nombre        #En esta linea esta el atributo del metodo, el self llama al atributo nombre y se le pone un igual al atributo
        self.__cursos=[]            #En esta linea se define una lista vacia la cual su nombre esta definido como cursos

    def agregarCurso(self,titulo):      #En esta linea se crea un metodo el cual es agregarCursos y su atributo es self y titulo
        self.__cursos.append(titulo)        #En esta linea se define como cursos y esta agrega a la lista vacia creada anteriormente en la clase Aprendiz y se le agrega al objeto titulo

    def getCursos(self):        #En esta linea se crea un metodo el cual getCursos busca el atributo 
        return self.__cursos    #retorna los cursos que fueron agregador en el metodo cursos

class Curso:            #En esta linea se crea una clase la cual esta definida como Curso
    def __init__(self,titulo):      #En esta linea se crea un metodo el cual tiene un __init__ y su atributos son self y titulo
        self.__titulo=titulo        #En esta linea esta el atributo del metodo el cual es titulo y es igual a ese mismo 

    def getTitulo(self):        #En esta linea se crea un metodo el cual es getTitulo y busca el atributo
        return self.__titulo    #retorna el titulo que ya tiene nuevos objetos y los cuales fueron agregados 
    
a=Aprendiz('Martha')        #Se crea un objeto el cual es a y es igual a la clase Aprediz su atributo era nombre y esta es Martha
c1=Curso('Python Intermedio')   #Se crea un objeto el cual es c1 este llama a la clase llamada Curso este tenia como atributo titulo, aqui se define como se llama su nombre es Python Intermedio
c2=Curso('Python Basico')       #Se crea un objeto el cual es c2 este llama a la clase llamada Curso este tenia como atributo titulo, aqui se define como se llama su nombre es Python Basico
c3=Curso('Introduccion a Java') #Se crea un objeto el cual es c3 este llama a la clase llamada Curso este tenia como atributo titulo, aqui se define como se llama su nombre es Introducción a Java

a.agregarCurso(c1)  #En esta linea llama a la clase creada agregarCurso el cual agrega el objeto C1 a aprendiz
a.agregarCurso(c2)  #En esta linea llama a la clase creada agregarCurso el cual agrega el objeto C2 a aprendiz
a.agregarCurso(c3)  #En esta linea llama a la clase creada agregarCurso el cual agrega el objeto C3 a aprendiz

print(a.getCursos()) #En esta linea imprime los cursos  que fueron agregados a la clase agregarCursos


for curso in a.getCursos():   #En esta linea se crea un ciclo for el cual recorre la clase curso, con el metodo getCursos
    print(curso.getTitulo())    #En esta linea imprime lo que encontro en la lista getTitulo