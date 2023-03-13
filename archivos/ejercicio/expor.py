from datos import *
import csv


listaEmpresa=[]
with open ('C:\\Users\\APRENDIZ\\Documents\\Yuri\\2560664\\archivos\\ejercicio\\txt') as info:
        equis=csv.reader(info)
        for e in info:
            holi=datos(e[0],e[1],e[2],e[3])
            listaEmpresa.append(holi)
    
print(listaEmpresa)
for holi in listaEmpresa:
    print(holi.datos())