'''Pida una cadena por teclado y diga cual es su valor al sumar sus codigos. Cual es el valor numerico de acuerdo a los códigos del alfabeto'''
def codigos_p(alfa):
    a=0
    for i in alfa:
        a+=ord(i)
    return a
print(codigos_p('los atardeceres son grandiosos'))






