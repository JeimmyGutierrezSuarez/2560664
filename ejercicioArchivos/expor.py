from datos import *
import csv


listaEmpresa=[]
with open ('C:\\Users\\arnol\\Documents\\Jeimmy G\\Samuel Padilla\\Repositorio\\2560664\\ejercicioArchivos\\empresas.csv') as info:
        equis=csv.reader(info)
        for e in equis:
            was=datos(e[0],e[1],e[2],e[3])
            listaEmpresa.append(was)
    
print(listaEmpresa)
for was in listaEmpresa:
    print(was.informacionEmpresa())

print('Menú')
print('1.indice')
print('2.ID de la organización')
print('3.Nombre de la Organización')
print('4.Sitio web de la organización')
escr=int(input('¿qué opción eliges?'))
for y in listaEmpresa:
    while escr == 1:
        print(y.informacionEmpresa())
#('C:\\Users\\arnol\\Documents\\Jeimmy G\\Samuel Padilla\\Repositorio\\2560664\\ejercicioArchivos\\empresas.csv')
'''si la persona  4 la informacion de la empresa
que quieres ver de la empresa 
organizacion de la empresa 7, '''