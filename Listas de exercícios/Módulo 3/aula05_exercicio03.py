# **3)** Soma de duas árvores binárias.
#Dado duas árvores binárias retorne uma que é a soma das duas como no exemplo:

import os
os.system('clear') or None

# arvore1 = [1,3,2,5,0,0,0]
# arvore2 = [2,1,3,0,4,0,7]

#arvores de tamanhos diferentes
# arvore1 = [1,3,2,5,None,None,None]
# arvore2 = [2,1,3,None,4,None,7]

arvore2 = [1,3,2,5,None,None,None,6,None,None,None] 
arvore1 = [2,1,3,None,4,None,7] 

arvore3 = []

if len(arvore1) != len(arvore2):

    if len(arvore1) < len(arvore2):
        #print('arvore1')
        diferenca = len(arvore2) - len(arvore1)
        for idx in range(diferenca):
            arvore1.append(None)

    else:
        #print('arvore2')
        diferenca = len(arvore1) - len(arvore2)
        for idx in range(diferenca):
            arvore2.append(None)

print(arvore1)
print(arvore2)


for posicao in range(len(arvore1)):
    if type(arvore1[posicao]) == int and type(arvore2[posicao]) == int:
        soma = arvore1[posicao] + arvore2[posicao]
    elif arvore1[posicao] == None and type(arvore2[posicao]) == int:
        soma = arvore2[posicao]
    elif type(arvore1[posicao]) == int and arvore2[posicao] == None:        
        soma = arvore1[posicao]
    else:
        soma = None

    arvore3.append(soma)

print(arvore3)
