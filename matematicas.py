"""
Programa que calcula una serie de operaciones Matematicas

    Factorial    
    Raiz Cuadrada
    Hipotenusa
    El area de un circulo
    El area de un cuadrado


"""
    
"""_summary_
funcion para calcular el factorial de un numero

Variable a pasar un numero y returna el factorial de ese numero

"""
def factorial(num): 
    if num < 0: 
        print("Factorial of negative num does not exist")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 


    """_summary_
    Calculo de la Raiz Cuadrada
    """
def cuadrada(num):
     raiz = num** 0.5
     return raiz

"""
    _summary_
    Calculo de la Hipotenusa 

    Returns:
        _type_: _description_
"""
def hipo(a,b):
    h = (a*a) + (b*b)
    return h

"""_summary_
   Calcular el area de un circulo

    Returns:
        _type_: _description_
 """

def area(r):
    pi = 3.141592
    a = pi * (r*r)
    return a
"""_summary_
funcion para calcular el factorial de un numero

 Variable a pasar un numero y returna el factorial de ese numero

    Returns:
        _type_: _description_
"""

"""_summary_
Funcion que calcula el area de un rectangulo
"""

def rectangulo(a,l):
    a1 = a * l
    return a1