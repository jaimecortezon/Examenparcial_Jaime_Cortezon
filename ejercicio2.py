lista = [18,50,210,80,145,333,70,30] 
#imprimir si es divisible entre 10 y menor que 200, si es >300 para bucle
for numero in lista:
    if (numero % 10 == 0) and (numero < 200):
        print(str(numero))
    elif (numero > 300):
        break

#ordenar la lista
lista.sort()
print(lista)

#devolver el indice de 145
lista2 = [8,50,210,80,333,70,30,145]
for index, numero in enumerate(lista2):
    if numero == 145:
        print(index)


