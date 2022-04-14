

def soma_inteiros(lista):
    soma = 0
    for x in lista:
        if type(x) == list:
            soma += soma_inteiros(x)
        else:
            soma += x
    return soma

listaGabarito = [[0, 3, 5, 1], 2, 3, [2, [5, 6, 7, [1, 4, 6]], 3], 2, [3, 5, 10, [6]]]
print (soma_inteiros(listaGabarito))




------------------------------------------------------------




lista1 =  [3,1,2,4,10,55,31,54]

def ordernacao(lista):
    listapares = []
    listaimpares = []
    

    for n in lista:
        if n%2 == 0:
            listapares.append(n)
        else:
            listaimpares.append(n)

    return listapares + listaimpares


print(ordernacao(lista1))


Complexidade O(n)

