''' Write a program that reads a positive integer, n, from the user and then displays the
sum of all of the integers from 1 to n. The sum of the first n positive integers can be
computed using the formula: suma = (n)(n + 1)/2'''
'''
def suma_hasta_n(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

n = int(input("Ingresa un número entero positivo: "))
resultado = suma_hasta_n(n)
print("La suma de los números del 1 al", n, "es:", resultado)
'''

def suma_hasta_n(n):
    suma = 0
    suma = n*(n+1)/2
    return suma

n = int(input("Ingresa un número entero positivo: "))
resultado = suma_hasta_n(n)
print("La suma de los números del 1 al", n, "es:", resultado)
