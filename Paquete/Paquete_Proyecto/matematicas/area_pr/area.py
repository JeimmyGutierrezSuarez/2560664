def a_tria():
    b=float(input('¿Cual es la base del triangulo?\n- '))
    h=float(input('¿Cual es la altura del triangulo?\n- '))
    a=b*h/2
    return a

def a_cuad():
    l1=float(input('¿Cual es el primer lado de tu cuadrado?\n- '))
    l2=float(input('¿Cual es el segundo lado de tu triangulo?\n- '))
    a=l1*l2
    return a

def a_rect():
    b=float(input('¿Cual es la base del rectangulo?\n- '))
    h=float(input('¿Cual es la altura del rectangulo?\n- '))
    a=b*a
    return a

def a_circle():
    r=float(input('¿Cual es el radio del circulo?\n- '))
    a=round(3.14*r**2,2)
    return a

def a_trapec():
    b1=float(input('¿Cual es la primera base de tu trapecio?\n- '))
    b2=float(input('¿Cual es la segunda base de tu trapecio?\n- '))
    h=float(input('¿Cual es la altura de tu trapecio?\n- '))
    a=round((b1+b2)*h/2,2)
    return a

def a_elipse():
    a=float(input('¿Cual es el primer radio del elipse?\n- '))
    b=float(input('¿Cual es el segundo radio del elipse?\n- '))
    c=round(3.14*a*b,3)
    return c