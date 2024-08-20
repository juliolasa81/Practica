'''Contar letras en una cadena 
Escribe un programa que cuente 
cuántas veces aparece una letra específica 
(por ejemplo, 'a') en la cadena "comercial".'''

palabra = "comerial"
letra_a = 'a'
contador = 0
for i in palabra:
    if i == letra_a:
        contador = contador + 1
print(contador)        



