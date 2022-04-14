'''1) Faça uma função que receba uma lista com n inteiros e retorne ela ordenada com os pares primeiros seguidos dos impares, por fim comente qual a complexidade do algoritmo feito.

Example 1:

Input: [3,1,2,4]

Output: [2,4,3,1]

Explanation: As saídas [4,2,3,1], [2,4,1,3], e [4,2,1,3] também seriam aceitas.

Example 2:

Input: [0]

Output: [0]'''


from numpy import sort


lista = [3,1,2,4]

def parImpar(lista):
    
    lista.sort()
    listapar = []
    listaimpar = []

    for i in lista:
        if i%2 == 0:
            listapar.append(i)
        else:
            listaimpar.append(i)

    return(listapar + listaimpar)


lista = [3,1,2,4]
var = parImpar(lista)
print(var)