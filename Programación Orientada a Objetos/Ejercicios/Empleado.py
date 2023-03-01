'''Escriba una clase Empleado que tenga como propiedades nombre, cargo, salario
escriba metodos contructores, setters y getters
escriba un método que permita calcular cuanto gana el empleado en una hora
un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
Un método que reciba una cantidad de horas extras y calcule el salario incementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide'''
class Empleado:
    def __init__(self,nombre,cargo,salario,hora):
        self.nombre=nombre
        self.cargo=cargo
        self.salario=salario
        self.hora=hora
    
    def getHora(self,hora):
        return ob.setSalario/hora

    def getNombre(self):
        return  self.nombre
    
    def getCargo(self):
        return self.cargo
    
    def getSalario(self):
        return self.salario

    
    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setCargo(self,cargo):
        self.cargo=cargo
    
    def setSalario(self,salario):
        self.salario=salario

    def setHora(self,hora):
        self.hora=hora

    

ob=Empleado('Carmen','Contadora',1300000,240)
print(ob.getNombre(),ob.getCargo(),ob.getSalario(),ob.getHora())
ob.setNombre('Maria')
ob.setCargo('Administradora')
ob.setSalario(1300000)
ob.setHora(240)
print(ob.getNombre(),ob.getCargo(),ob.getSalario(),ob.getHora())     #sueldo minimo divicido por 240


#
#variable clase que sea un contador











