#Jesús Eduardo Rico Sandoval
def iva(n):
    ''' funcion basica para calcular el IVA de una cantidad dada'''
    print("El monto es: ", n )
    iva = n - (n/ 1.16)
    print("IVA (16%): ", iva)
    print("La cantidad sin IVA es: ", n - iva)
