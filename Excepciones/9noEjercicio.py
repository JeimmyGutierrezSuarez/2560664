'OverFlowError'
def over(n1):
    try:
        total=1E250**n1
        return total
    except OverflowError:
        print('El numero ha superado su tamaño en memoria')
    except:
        print('El programa ocupa otro error')
over(2)