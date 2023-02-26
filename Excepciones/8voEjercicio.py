'KeyError'
publicaciones=[{'Fotos': 3, 'Me gusta': 21, 'comentarios': 2}, 
              {'Me gusta': 13, 'comentarios': 2, 'compartido': 1}, 
              {'comentarios': 4, 'compartido': 2}, 
                 {'Fotos': 8, 'compartido': 1}]
s=0
for i in publicaciones:
    try:
        s+=i['Fotos']
    except KeyError:
        print('No contiene la clave "Fotos"')
print('El total de fotos publicadas es',s)