# python -m doctest E:\software\PYTHON\platzy\unitTesting\excercice01\calculator.py
# lo anterior para probar la prueba con secciones interactivas


def sum(a, b):
    """  
    >>> sum(5,7)
    1
    
    >>> sum(4,-4)
    1
    """
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    """ 
    >>> div(10,0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    """
    if a == 0:
        raise ValueError('Division por 0 no esta permitida')
    return a / b