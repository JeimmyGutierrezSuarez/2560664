import sqlite3
with sqlite3.connect('C:\\Users\\AdminSena\\Documents\\Yuri\\2560664\\ProyectoHotel\\BD PROYECTO.db') as hab:
    micursor1=hab.cursor()
    
def Insertacion_tb_habitaciones (conexion,tabla,id_res,idTipoHab,canHab,NumPersona):
    micursor=conexion.cursor()
    sentecia=f'INSERT INTO  {tabla} VALUES ("{id_res}","{idTipoHab}", "{canHab}", "{NumPersona}")'
    micursor.execute(sentecia)
    hab.commit()
    print('fue un exito')
Insertacion_tb_habitaciones(hab,'tb_habitaciones',1,1,1,2)

def Seleccón_tb_habitaciones (conexion,tabla,):
    micursor=conexion.cursor
    sentecia=f'SELECT * FROM {tabla} '
    print(micursor.excute(sentecia.fetchall))
