'''Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, 
etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores'''
nota=float(input('Ingresa tu nota final de semestre: '))
bajo= 0.1 - 5.9
basico= 6.0 - 6.9
alto= 7.0 - 8.9
superior= 9.0 - 10
if nota<5.9:
    print('Tu nota es baja')
elif nota<=6.9:
   print('Tu nota es basica')
elif nota<=7.0:
    print('Tu nota es alta')
elif nota<9.0:
    print('Tu nota es superior')