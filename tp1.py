#trabajo practico 1.
#Debera resolver los ejercicios 5 y 22 de la guia de ejercicios de recursividad del libro, subirlos a github y pasar el link en la entrega.
romano = input('ingrese el numero romano: ').upper()
def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }
    
    if len(romano) == 0:
        return 0
    
    if len(romano) == 1:
        return valores[romano]
    
    if valores[romano[0]] < valores[romano[1]]:
        return -valores[romano[0]] + romano_a_decimal(romano[1:])
    else:
        return valores[romano[0]] + romano_a_decimal(romano[1:])
print('el numero es: ', romano_a_decimal(romano))     