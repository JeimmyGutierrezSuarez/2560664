'''def funcion (lista):
    list2=[]
    for i in my_list:
        if i in list2:
            list2.append(i)
    print(list2)
my_list=[1,2,4,4,1,4,2,6,2,9]
funcion(my_list)'''
        #Primer ejercicio
def funcion(familia):
    while True:
        a=input('Ingresa los nombres de tu familia, o pulsa la tecla "Enter" para no agregar mas nombres: ')  
        familia.append(a) 
        if a == "":
            break
    print('tu familia es: ',familia[:-1])
familia=[]
funcion(familia)

        #Segundo ejercicio
def funcion(lista):
    for i in range (1000,3000+2):
        if (i%2==0):
            lista.append(i)
    print('los numero pares en el rango de 1000 a 3000 son: ',lista)
lista=[]
funcion(lista)

        #Tercer ejercicio
def funcion(lista):
    for i in range (1,10000+2):
        if (i%2!=0):
            lista.append(i)
    print('los numero impares en el rango de 1 a 10000 son: ',lista)
lista=[]
funcion(lista)