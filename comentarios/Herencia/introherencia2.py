class A1:       #En esta linea se crea la clase la cual su nombre es A1
    def __init__(self):     #En esta linea hay un constructor ya que contiene __init__ su parametro son self el cual siempre se debe escribir
        pass        #pass es un marcador de posición que evita que el programa emita un mensaje de error
    def saludo(self):       #En esta linea se crea un metodo el cual es Saludo y su parametro es self
        print('Hola desde A1')  #En esta linea imprime un mensaje el cual es Hola desde A1 desde el metodo Saludo

class A2:   #Aqui se crea otra clase la cual su nombre es A2
    def __init__(self): #En esta linea hay un constructor ya que contiene __init__ y su parametro es self
        pass        #pass es un marcador de posición que evita que el programa emita un mensaje de error
    def saludo(self):   #En esta linea se crea un metodo el cual su nombre es saludo y como para metro es self
        print('Hola desde A2')  #En esta linea imrpime Hola desde A2 desde la clases A2 y su metodo saludo


class B(A2,A1):     #En esta linea se crea la clase, la cual es B esta es un clase  jerarquica ya que tiene la clase A2 y A1
    def __init__(self): #En esta linea hay un constructor ya que contiene __init__ y su parametro es self
        pass        #pass es un marcador de posición que evita que el programa emita un mensaje de error
    def saludo(self):#En esta linea se define el metodo el cual es saludo y su parametro es self
        print('Hola desde B')      #En esta linea imprime un mensaje el cual es Hola desde B, desde la clase B y metodo saludo
    def __str__(self):      #Este metodo hace que pueda verificar si tiene caracteres de texto
        return 'Soy un objeto de la clase B'    #retorna un mensaje el cual es Soy un objeto de la clase B este metodo esta con la clase __str__
obj=B() #Este objeto es de la clase B y retorna el metodo __str__ ya que muestras los caracteres que contiene
print(obj.__str__())    #En esta linea imprime el objeto que ya fue definido el cual es obj.__str__ y imprime el mensaje que fue definido en el metodo __str__
#obj.saludo()
#obj.saludo()


# cad="sena"
# lista=[1,2,3]
# print(cad.__str__())
# print(lista.__str__())