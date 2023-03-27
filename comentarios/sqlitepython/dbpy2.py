import sqlite3

with sqlite3.connect('C:\\Users\\AdminSena\\Documents\\Yuri\\2560664\\comentarios\\sqlitepython\\conpython.db') as con:
    micursor=con.cursor()
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"
    #print(micursor.execute(sentencia).fetchall())

def miselect(conexion,tabla,campo,operador,dato):
    micursor=conexion.cursor()
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"
    print(sentencia)
    print(micursor.execute(sentencia).fetchall())

miselect(con,'alumno','email','=','dbrabon2@irs.gov')


def modificar (conexion,tabla,campo,dato,id):
    micursor=conexion.cursor()
    sentencia=f"Update {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.execute(sentencia)
    con.commit()
    print('modificación Exiitosa')

def eliminar (conexion,tabla,campo,dato):
    micursor=conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execuse(sentencia)
    con.commit()
    print('eliminacion exitosa')