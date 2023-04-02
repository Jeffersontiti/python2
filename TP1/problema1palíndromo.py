#Se necesita crear un programa que reciba del usuario una frase y decida si esa
#frase es un palíndromo o no. Un palíndromo se puede leer de igual forma de
#izquierda a derecha, que de derecha a izquierda. Ejemplo: "Anita lava la tina".

##pedirle al usuario una frase

##para cada palabra revisar si es palindromo

##si ES palindromo mostrar
  #imprimir si es polindromo

##si NO es polindromo 
  #imprimir no es polindromo
  
def es_palindromo(frase):
    frase = frase.lower().replace(" ", "")
    return frase == frase[::-1]

frase = input("Ingrese una frase: ")
if es_palindromo(frase):
    print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")