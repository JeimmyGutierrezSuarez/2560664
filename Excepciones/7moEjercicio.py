'ModuleNotFoundError'
def i_e(num1):
    try:        
        import mat
        total=mat.sqrt(num1)
        print(total)
    except ModuleNotFoundError:
        print('El modulo que importaste no pudo ser importado o tal vez no existe')
    except:
        print('El programa sufre de otro ')    
    else:
        print(total)
i_e(2)