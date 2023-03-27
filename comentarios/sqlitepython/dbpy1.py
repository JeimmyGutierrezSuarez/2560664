import sqlite3
with sqlite3.connect('C:\Users\AdminSena\Documents\Yuri\2560664\comentarios\sqlitepython\\conpython.db')as con:
    micursor=con.cursor()
    sentencia="SELECT nombre,apellido FROM alumno;"
    print(micursor.execute(sentencia).fetchmany(10))

#print()
