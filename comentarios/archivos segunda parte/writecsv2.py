import csv  #se importa un aclase csv
diccio=[                #Se crea una variable diccio la cual es una lista con diccionarios 
    {'name':'Alice','age':18},      #se crea un diccionario con cuatro 
    {'name':'Bob','age':19},
    {'name':'John','age':17}
]
header=['name','age']

with open('archivos/people.csv','w') as csvfile:
    writer=csv.DictWriter(csvfile,fieldnames=header)
    writer.writeheader()
    writer.writerows(diccio)