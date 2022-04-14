# Escreva um programa Python para verificar se uma 
# determinada árvore binária é uma árvore binária completa ou não.

import os
os.system('clear') or None

arvore_b_completa = [3,9,20,None,None,15,7]
arvore_n_completa = [3,9,20,None,None,None,7]
arvore_9_completa = [3,None,20,None,None,15,7]

contador = 0

for idx in range(1,len(arvore_9_completa),2):
    #print(idx)
    print(type(arvore_9_completa[idx]))
    print(type(arvore_9_completa[idx+1]))
    #if type(arvore_b_completa[idx]) == type(arvore_b_completa[idx+1]):
        

