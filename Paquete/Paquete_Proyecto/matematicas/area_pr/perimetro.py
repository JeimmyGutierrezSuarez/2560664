def p_trian():
	l1=float(input('¿Cual es el primer lado de tu triangulo?\n-'))
	l2=float(input('¿Cual es el segundo lado de tu triangulo?\n-'))
	l3=float(input('¿Cual es el tercer lado de tu triangulo?\n-'))
	if l1==l2 and l3==l2 and l1==l3:
		total=l1+l2+l3
		print('Tu triangulo es equilatero y su perimetro es:',total)
	elif l1==l2 or l1==l3 or l2==l3:
		total=l1+l2+l3
		print('Tu triangulo es isoceles y su perimetro es:',total)
	else:
		total=l1+l2+l3
		print('Tu triangulo es escaleno y su perimetro es:',total)

def p_cuad():
	lados=float(input('¿Cuanto miden todos los lados de tu cuadrado?\n-'))
	total=lados*4
	return total

def p_rect():
	b=float(input('¿Cual es la base del rectangulo?\n-'))
	h=float(input('¿Cual es la altura del rectangulo?\n-'))
	total=str(2*(b+h))
	return total

def p_circle():
	dia=float(input('¿Cual es el diametro del circulo?\n-'))
	p=round(3.14*dia,2)
	return p

def p_trapec():
	a=float(input('¿Cual es el primer lado del trapecio?\n-'))
	b=float(input('¿Cual es el segundo angulo de tu trapecio?\n-'))
	c=float(input('¿Cual es el tercer angulo de tu trapecio?\n-'))
	d=float(input('¿Cual es el cuarto lado de tu trapecio?\n-'))
	total=a+b+c+d
	return total