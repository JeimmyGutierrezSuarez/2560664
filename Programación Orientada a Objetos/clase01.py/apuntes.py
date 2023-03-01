class Persona:
    nacionalidad='Colombia' #sera el mismo valor para la clase persona
    def __init__(self,nombre,documento):  #constructro tiene un init, con parametros,el constructor siempre debe ir dentro de la clase
        self.__nombre=nombre       #self.__nombre es una instacia  =nombre igual es el parametro
        self.domento=documento
        print('Activando constructor')

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def metodo(self):
        print('Soy un método')


ob=Persona('Ana')
ob.mail='oso@gmail.com'
print(ob.mail)

print(ob.getNombre())
ob.setNombre('Maria')
print(ob.getNombre())

#las variables de instacia siempre se declara en el constructor
#per1=persona() per1 es una instancia
#metodo es una funccion que esta dentro de una clase
#variables de  insttacia (contructor, metodo, ob)








def hora






