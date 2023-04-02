#Cree una solución que permita al usuario ingresar un número entero. Dado dicho
#número, el programa debe determinar si los dígitos de este número se pueden
#ordenar de forma tal que el resultado sea un múltiplo de 5.









def es_multiplo_de_5(numero):
    # Convierte el número en una lista de dígitos
    digitos = list(str(numero))
    
    # Ordena los dígitos de manera ascendente
    digitos.sort()
    
    # Verifica si el último dígito es 0 o 5, lo que indica que el número es un múltiplo de 5
    if digitos[-1] in ['0', '5']:
        return True
    
    # Si el último dígito no es 0 o 5, verifica si existe un 0 y si los demás dígitos suman un múltiplo de 5
    if '0' in digitos:
        digitos_sin_ceros = [int(d) for d in digitos if d != '0']
        if sum(digitos_sin_ceros) % 5 == 0:
            return True
    
    # Si ninguna de las condiciones anteriores se cumple, el número no es un múltiplo de 5
    return False

# Solicita al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Verifica si el número es un múltiplo de 5
if es_multiplo_de_5(numero):
    print("Los dígitos de este número se pueden ordenar de forma tal que el resultado sea un múltiplo de 5")
else:
    print("Los dígitos de este número no se pueden ordenar de forma tal que el resultado sea un múltiplo de 5")
