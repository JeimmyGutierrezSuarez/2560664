from Conductor import *     #De conductor importa todo,from quiere decir que busca el archivo conductor, import este importa todo lo que esta en el archivo conductor
from Carga import *        #De carga importa todo,from quiere decir que busca el archivo carga, import este importa todo lo que esta en el archivo carga
lista=[]        #Se crea una lista vacia y su nombre es lista 
with open('poo-archivos/listado.txt','r') as flujo:      #En esta linea se crea un bloque de codigo para manipular el archivo que esta adentro de los parentesis,la letra r que aparce dentro de apostrofes quiere decir que lea el archivo solicitado, el as que aparece cambia el nombre del archivo por flujo
    for ob in flujo:        #En esta linea ob recorre el archivo flujo
        lista.append(ob)    #Agrega lo que ob encontro en el archivo flujo en una lista que ya se habia definido como vacia en la linea
i=0     #i es un contador que empieza en cero
for ob in lista:    #En esta linea ob recorre lo que hay en la lista
    lista[i]=ob.rstrip()    #La i hace recorrido en la lista en la posición 0 y este elimina los carateres especiales que vaya encontrando 
    i+=1        #La i mas uno va contado el recorrido que esta haciendo en la lista
print(lista)    #Imprime la lista con los caracteres especiales eliminados
#placa, nombre,doc, cap, ejes
lautos=[]   #Esta es una lista vacia y su nombre es lautos
for ob in lista:    #ob hace el recorrido en la lista la cual eliminaron sus caracteres especiales eliminados
    #for x in ob.split(','):
    lautos.append(ob.split(','))    #Esta agrega en la lista lautos y en el recorrido que hizo se le agregan comas
cargas=[]      #Esta es una lista vacia y su nombre es cargas
print(lautos)   #Imprime la lista lautos agregando lo que habia en la lista y separadas por comas
for i in range(len(lautos)):    #la i hace el recorrido en el rango de la longitud de la lista lautos
    #print(lautos[i][0])    
    p=lautos[i][0]      #P hace referencia a la placa. Este hace el recorrido de la lista lautos en la posicion cero
    n=lautos[i][1]      #N hace referencia al nombre. Este hace el recorrido de la lista lautos en la posicion uno
    d=lautos[i][2]      #D hace referencia al documento. Este hace el recorrido de la lista lautos en la posicion dos
    c=lautos[i][3]      #C hace referencia a la capacidad. Este hace el recorrido de la lista lautos en la posicion tres
    e=lautos[i][4]      #E hace referencia a ejes. Este hace el recorrido de la lista lautos en la posicion cuatro
    con=Conductor(n,d)      #Con es igual a conductor y sus variables son n (nombre) y d (documento) esta es la información del conductor
    obj=Carga(p,con,c,e)    #Obj es igual a la carga del vehiculo sus variables son p (placa) con (información de conductor) c (capacidad) e (ejes)
    cargas.append(obj)      #En esta linea obj agrega la informacion en la lista cargas

print(cargas)    #Imprime la lista con los elementos agregados 
# 
# for ob in lautos:
    
#     #for x in ob:
#      #   print(x)
#         # p=x[0]
#         # n=x[1]
#         # d=x[2]
#         # c=x[3]
#         # e=x[4]
#         # con=Conductor(n,d)
#         # obj=Carga(p,con,c,e)
#         # cargas.append(obj)
# print(cargas)