'''d={"gato":'chat','perro':'chien'.'caballo':'cheval'}
funcion (d)'''

        #Primer ejercicio

def agregar (dictionary):
    for f in dictionary.items():
        print (f)
d={'i':1,'o':2}
o={'e':3,'p':4}
o.update (d)
print(d,o)


        #Segundo ejercicio
def traduccion (dictionary):
    for i in dictionary.values():
        print(i)
saludos={'hola':'ciao',
'adios':'addio',
'buenos días':'guete morge'}
traduccion(saludos)


        #Tercer ejercicio
def traduccion(dictionary):
    for i in dictionary.keys():
        print (i)
ingles={'apple':'manzana',
    'orange':'naranja',
    'strawberry':'fresa'}
traduccion(ingles)