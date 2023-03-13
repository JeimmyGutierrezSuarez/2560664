from Carga import *     #De carga importa todo,from quiere decir que busca el archivo carga, import este importa todo lo que esta en el archivo Carga
from Conductor import *    #De carga importa todo, from quiere decir que busca el archivo conductor, import este importa todo lo que esta en el archivo conductor
# c1=Conductor('Luis',12345)
# carga1=Carga('aaa-123',c1,5,2)
# print(carga1)
nomConductor=input('Ingrese nombre del conductor: ')    #nomConductor es una variable la cual tiene un input y este es para poder digitar en pantalla, este va a imprimir un mensaje el cual Ingrese nombre del conductor.
docConductor=int(input('Ingrese documento del conductor: '))    #docConductor es una variable la cual tiene un int, apar que ingrese un numero entero, input este es para poder digitar en pantalla, este va a imprimir un mensaje el cual es ingrese documento del conductor.
placa=input('ingrese placa: ')  #placa es una variable la cual tiene un input, este es para poder digitar en pantalla, este va a imprimir un mensaje el cual es ingrese placa.
capacidad=input('ingrese capacidad en toneladas: ') #capacidad es una variable la cual tiene un input, este es para poder digitar en pantalla, este va a imprimir un mensaje el cual Ingrese capacidad de toneladas.
ejes=input('ingrese numero de ejes: ')  #ejes es una variable la cual tiene un input, este es para poder digitar en pantalla, este va a imprimir un mensaje el cual Ingrese numero de ejes.
c1=Conductor(nomConductor,docConductor) #c1 es una variable, esta llama a la clase conductor, y guarda las variales nomConductor y docConductor.
obCarga=Carga(placa,c1,capacidad,ejes)  #obCarga es una variables, esta llama a la calase Cargar y guarda las variables placa, c1 (conductor), capacidad y ejes.
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento())  #cadConductor es una variable la cual llama a la variable obCarga y getConductor retorna el nombre del conductor el cual fue ingresado, mas concatena el nombre y documento, el str sirve para que convierte los numeros en letras y estos se puedan concatenar, getDocumento retorna el documento ingresado

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes())     #cadCarga es una variable la cual llama a la variable obCarga y getPlaca retorna la placa del conductor el cual fue ingresado, mas concatena la placa y los atributos del conductor, el str sirve para que convierte los numeros en letras y estos se puedan concatenar, getCapacidad retorna la capacidad ingresada, hay otro mas para que concatene la placa, el conductor, la capacidad y los ejes ingresados, getejes retorna los ejes ingresados.

with open('C:\\Users\\arnol\\Documents\\Jeimmy G\\Samuel Padilla\\Repositorio\\2560664\\Poo-archivos\\listado.txt','a') as flujo: 
    #En esta linea se crea un bloque de codigo para manipular el archivo que esta adentro de los parentesis,la letra a que aparece dentro de apostrofes quiere decir que agregue objetos al archivo solicitado, el as que aparece cambia el nombre del archivo por flujo
    flujo.write(cadCarga+'\n')  #flujo.write quiere decir que en el archivo se pueda escribir dentro de el, cad.carga es para que se vaya agregando y cada que se agregue infromación diferente vaya a otra linea