def f_suma():
	n1=int(input('¿Cual es tu primer numerador?\n-'))
	d1=int(input('¿Cual es tu primer denominador?\n-'))
	n2=int(input('¿Cual es tu segundo numerador?\n-'))
	d2=int(input('¿Cual es tu segundo denominador?\n-'))
	p1=(d1*d2)
	p2=(d1*n2)+(d2*n1)
	print(f'El resultado de la suma es {p2}/{p1}')

def f_resta():
	n1=int(input('¿Cual es tu primer numerador?\n-'))
	d1=int(input('¿Cual es tu primer denominador?\n-'))
	n2=int(input('¿Cual es tu segundo numerador?\n-'))
	d2=int(input('¿Cual es tu segundo denominador?\n-'))
	p1=(d1*d2)
	p2=(d2*n1)-(d1*n2)
	print(f'El resultado de la resta es {p2}/{p1}')

def f_multipli():
	n1=int(input('¿Cual es tu primer numerador?\n-'))
	d1=int(input('¿Cual es tu primer denominador?\n-'))
	n2=int(input('¿Cual es tu segundo numerador?\n-'))
	d2=int(input('¿Cual es tu segundo denominador?\n-'))
	p1=(d1*d2)
	p2=(n1*n2)
	print(f'El resultado de la multiplicacion es {p2}/{p1}')

def f_division():
	n1=int(input('¿Cual es tu primer numerador?\n-'))
	d1=int(input('¿Cual es tu primer denominador?\n-'))
	n2=int(input('¿Cual es tu segundo numerador?\n-'))
	d2=int(input('¿Cual es tu segundo denominador?\n-'))
	p1=(d1*n2)
	p2=(d2*n1)
	print(f'El resultado de la division es {p2}/{p1}')
