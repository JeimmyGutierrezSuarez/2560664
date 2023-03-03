'''Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario
escriba metodos contructores, setters y getters
escriba un método que permita calcular cuanto gana el empleado en una hora
un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide'''
class Empleado:
    contador=0
    def __init__(self,nombre,cargo,salario,extras):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        self.__extras=extras
        self.__class__.contador+=1

    def getNombre(self):
        return  self.__nombre
    
    def getCargo(self):
        return self.__cargo
    
    def getSalario(self):
        return self.__salario

    
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def setCargo(self,cargo):
        self.__cargo=cargo
    
    def setSalario(self,salario):
        self.__salario=salario

    def Hora(self):
        hora=self.__salario//160
        return hora
    
    def incremento(self):
        if self.__salario==1160000:
            incremento_salario=self.__salario*16.3//100
            return incremento_salario
        elif self.__salario>1160000:
            incremento_mas=self.__salario*13.3//100
            return incremento_mas
        elif self.__salario<1160000:
            return 'trabajo informal'

    def extras(self):
        if self.__extras<=10 and self.__extras>=0:
            t=self.__extras*self.__salario//160
            return t
        else:
            return 'has accedido las horas extras'

ob=Empleado('Luis','panadero',900000,5)
print(ob.contador)
print(ob.getNombre(),ob.getCargo(),ob.getSalario(),ob.Hora(),ob.incremento(),ob.extras())
ob=Empleado('Arnold','gerente de riesgos',4500000,3)
print(ob.contador)
print(ob.getNombre(),ob.getCargo(),ob.getSalario(),ob.Hora(),ob.incremento(),ob.extras())

#variable clase que sea un contador











