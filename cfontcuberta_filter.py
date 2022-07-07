"""Script que utilizando la funcion Filter de una lista,
  devuelva aquellos que son primos
    
"""


def es_primo(n):
    """Funcion que determina si un numero es primo

    Args:
        n (int): numero entero que se pasa a la funcion

    Returns:
        lista:lista de todos los numeros que son primos
    """
    return n%2 != 0 

# definicion de la lista de numeros
lista = [1,2,3,3,4,5,5,6,7,8,10,12,14,15,17,25]
# utilizacion de filter para hallar los primos

primo = list(filter(es_primo, lista))
print(primo)

