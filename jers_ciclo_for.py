#Jesús Eduardo Rico Sandoval
"""Se imprime 0 por cada vez que el usuario ingrese el valor de la funcion"""
"""ademas de ir agregando en el rango una cantidad de 2 para cada renglon"""
def navidad(n): 
    n *= 2 
    print(*[('0' * x).center(n - 1) for x in range(1, n, 2)], sep = '\n\n') 
    
