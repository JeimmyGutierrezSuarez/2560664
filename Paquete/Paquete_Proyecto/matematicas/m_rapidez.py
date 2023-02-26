def metros_seg():
	x=float(input('¿Cuantos metros recorrio en total?\n-'))
	y=float(input('¿En cuantos segundos recorrio dicha cantidad de metros?\n-'))
	total=round(x/y,1)
	return total

def km_hr():
	x=float(input('¿Cuantos Kms recorrio en total?\n-'))
	y=float(input('¿En cuantos horas recorrio dicha cantidad de Kms?\n-'))
	total=round(x/y,1)
	return total

def mts_m():
	x=float(input('¿Cual es la distancia en metros/Seg?\n-'))
	y=float(input('¿En cuantos tiempo recorrio dicha distancia?\n-'))
	total=round(x*y,1)
	return total

def hkmh_km():
	x=float(input('¿Cuantas horas tardo para llegar al destino?\n-'))
	y=float(input('¿Cual fue su velocidad media en km/h?\n'))
	total=round(x*y,1)
	return total
