import sqlite3      #En esta linea se importa squlite3 para poder utilizar su sintaxis
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
con=sqlite3.connect('C:\Users\AdminSena\Documents\Yuri\2560664\comentarios\sqlitepython\\conpython.db')    #Con es una variable la cual contiene, un conector con sqlite y se le da una ruta absoluta
print(type(con))    #Imprime el tipo de dato que es con la cual es la conexion 
micursor=con.cursor()   #la variable micursor recorre las filas que hay en la tabla creada 
print(type(micursor))   #imprime el tipo de dato que es micursor
sentencia="SELECT * from alumno;"
micursor.execute(sentencia)
for fila in micursor.fetchall():
    print(fila[0])
    print(fila[1])
    print(fila[2])
    print(fila[3])
    print('-'*50)