class Curso:        #En esta linea se crea la clase la cual es Curso
    def __init__(self,titulo):   #En esta linea hay un constructor ya que contiene __init__ sus parametros son self el cual siempre se debe escribir, su otro parametro es titulo.
        self.__titulo=titulo    #En esta linea esta el atributo del metodo, el self llama al atributo titulo y se le pone un igual al atributo

    def getTitulo(self):    #En esta linea se crea un metodo el cual es getNombre este busca el atributo 
        return self.__titulo       #retorna el 

class Aprendiz:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__cursos=[]

    def agregarCurso(self,nombreCursito):
        cursito=Curso(nombreCursito)
        self.__cursos.append(cursito)

    def getCursos(self):
        return self.__cursos
    
ap=Aprendiz('Sofia')
ap.agregarCurso('Python Basico')
ap.agregarCurso('Python Intermedio')

for c in ap.getCursos():
    print(c.getTitulo())
