"""Multiplicar cada elemento de una lista por 2
Escribe un programa que multiplique cada elemento de la lista [1, 2, 3, 4, 5] por 2 y 
almacene el resultado en una nueva lista. Imprime la nueva lista."""
elemento=[1,2,3,4,5]
nueva_lista=[]
for i in elemento:
    multiplo=i*2
    nueva_lista.append(multiplo)
print(f'Nueva lista {nueva_lista}')

