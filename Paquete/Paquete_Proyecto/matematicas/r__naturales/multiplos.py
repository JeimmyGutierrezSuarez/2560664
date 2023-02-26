def multiplo(x):
	multiplo=[]
	for i in range(2,x+1):
		if x%i==0:
			multiplo.append(i)
	print(multiplo)

def suma_multiplos(x):
	s=0
	for i in range(1,x+1):
		if x%i==0:
			s+=i
	return s

def comparacion_multiplos(x):
	s=0
	suma=[]
	multiplos=[]
	suma1=[]
	for i in range(1,x+1):
		if x%i==0:
			s+=i
		suma.append(s)
		repeticiones=0
		if s not in suma1:
			repeticiones+=1
			if repeticiones<=1:
				suma1.append(s)
	print(suma1)
	for i in range(1,x+1):
		if x%i==0:
			multiplos.append(i)
	print(multiplos)
	for i in suma1:
		for j in multiplos:
			if i==j:
				print('El multiplo',j,'es igual a la suma de uno de los multiplos de',x,'ese numero es',i)

def gnumeros_multiplo():
	while True:
		x=int(input('\nIndica el numero al que deseas hallar el multiplo (0 para salir) '))
		if x==0:
			break
		for i in range(1,x+1):
			if x%i==0:
				print(i,end=',')

def comparacion_divisiores():	
	lista=[]
	lista1=[]
	x=int(input('Ingresa tu primer numero: '))
	y=int(input('Ingresa tu segundo numero: '))
	for i in range(2,x+1):
		if x%i==0:
			lista.append(i)
	for j in range(2,y+1):
		if y%j==0:
			lista1.append(j)
	for i in lista:
		if i in lista1:
			total=x+y
			print('Ya que los dos cuentan con almenos un divisor en comun, se realiza la suma de ambos que es:',total)
		else:
			print('Los numeros no tienen divisores en comun')
