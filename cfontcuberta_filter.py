"""Script que utilizando la funcion Filter de una lista,
  devuelva aquellos que son primos
    
"""


"""Funcion que determina l lista de numeros primos
"""
def es_primo(n):
    return n%2 != 0 

# definicion de la lista de numeros
lista = [1,2,3,3,4,5,5,6,7,8,10,12,14,15,17,25]
# utilizacion de filter para hallar los primos

primo = list(filter(es_primo, lista))
print(primo)

