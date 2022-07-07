"""Calcular algunas operaciones matematicas

**Atributos**
--------------
        **ele1 :**
              operador para el calculo de un solo numero 
        **ele2 :** 
              cuando se requieren mas de una variable

**Metodos**
-------------

factorial
         Calcula el factorial de un numero
cuadrada
        calcula la raiz cuadrada de un numero
Hipo 
        Calcula la hipotenusa
area
        Calcula el area de un circulo

rectagunlo
        Calcula el area de un rectangulo

**Ejemplo**
------------
>>>>>factorial(5)
>>>>>>cuadrada(3)
>>>>>>hipo(5,3)
>>>>>>>area(3)
>>>>>>>>rectangulo(5,4)

"""


class matematicas:
    """Construccion de la clase para calcular algunas 
       operaciones matematicas
    """
    def __init__(self,ele1,ele2):
        self.ele1 = ele1
        self.ele2 = ele2

    def factorial(self,ele):
        """funcion que calcula el factorial de un numero

    Args:
        ele (self): argumento por defecto

    Returns:
        fact: el factorial del numero
    """
        if self.ele1  < 0: 
            print("Factorial de un numero negarivo no existe")
        elif self.ele1 == 0: 
            return 1
        
        else: 
            fact = 1
        while(self.ele1 > 1): 
            fact *= self.ele1
            self.ele1 -= 1
        return fact 


    def cuadrada(self,ele):
        """funcion que calcula la raiz cuadrada de un numero

    Args:
        ele : numero a calcular

    Returns:
        raiz: la raiz cuadrada del numero
    """
        raiz = self.ele1** 0.5
        return raiz



    def hipo(self,ele):
        """Funcion que calcula la hipotenusa

    Args:
        ele :  valores a calcular

    Returns:
        hipo: retorna la hipotenusa
    """
        h = (self.ele1**2) + (self.ele2**2)
        return h


    def area(self,ele):
        """funcion que calcula el area de un circulo
       se toma PI = 3.141592

    Args:
        ele : radio del circulo

    Returns:
        ele : el area del circulo
    """
        pi = 3.141592
        a = pi * (self.ele1**2)
        return a


    def rectangulo(self,ele):
        """Funcion que calcula el area de un rectagunlo

    Args:
        ele:   se pasa el ancho y largo

    Returns:
       area : devuelve el area del rectangulo
    """
        a1 = self.ele1 * self.ele2
        return a1