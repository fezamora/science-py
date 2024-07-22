import math
def height_ball(v,t,g=9.81):
    """
    Funcion que calcula la altura de una bola en movimiento vertical.
    Argumentos: 
    #velocidad inicial v 
    #tiempo t
    #aceleracion de la gravedad g = 9.81 m/s^2 
    """
    if v>=0 and t>=0 and t<= 2*v/g:
        y = v*t -0.5*g*t**2
        return y
    else: 
        raise ValueError("Parece que no ingreso numeros adecuados")

def time_ball(v,y,g=9.81):
    """
    Funcion que calcula los tiempos en el que una bola con velocidad inicial v lanzada al aire alcanza un altura y en movimiento vertical.
    La funcion devuelve una tupla de dos elementos que son los 2 tiempos.
    Argumentos: 
    #velocidad inicial v
    #altura y
    #aceleracion de la gravedad g = 9.81 m/s^2  
    """
    assert(v>=0)
    t1 = (v - math.sqrt(v**2- 2*g*y))/g
    t2 = (v + math.sqrt(v**2- 2*g*y))/g
    if t1>=0 and t2>=0:
        return (t1,t2)
    else:
        return     

  