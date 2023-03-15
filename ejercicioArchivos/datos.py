class datos:
    def __init__(self, id, organizacion,nombre,sitio_web):
        self.__id=id
        self.__organizacion=organizacion
        self.__nombre=nombre
        self.__sitio_web= sitio_web 

    def informacionEmpresa(self):
            return self.__id+' '+ self.__organizacion+' '+ self.__nombre+' '+self.__sitio_web
        