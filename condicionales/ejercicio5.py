'''En un juego de preguntas a las que se responde “Si” o “No” gana quien 
responda correctamente las tres preguntas. Si se responde mal a cualquiera de 
ellas ya no se pregunta la siguiente y termina el juego. Las preguntas son:'''

no='no'
si='si'
pregunta_uno=input('¿Colon descubrió América?: ')
if pregunta_uno==si:
    print('La respuesta es correcta')
elif pregunta_uno==no:
    quit(print('La respuesta es incorrecta'))
pregunta_dos=input('¿La independencia de Colombia fue en el año 1810?: ')
if pregunta_dos==si:
    print('La respuesta es correcta')
elif pregunta_dos==no:
    quit(print('La respuesta es incorrecta'))
pregunta_tres=input('¿The Doors fue un grupo de rock Americano?: ')
if pregunta_tres==si:
    print('La respuesta es correcta')
elif pregunta_tres==no:
    quit(print('La respuesta es incorrecta'))
