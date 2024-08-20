'''Sumar los elementos de una lista
Escribe un programa que sume todos los elementos de la lista
[1, 2, 3, 4, 5] utilizando un bucle for y que imprima la suma.'''

lista=[1,2,3,4,5]
resultado = 0
for i in lista:
    resultado = resultado + i
print(f'El resultado es: {resultado}')
