
linhas = 10
colunas = 8
import numpy as np
matriz = np.random.randint(0, 2, size=(linhas,colunas))

print("Matriz = ")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()

def tamanho_rio (matriz, i, j):
    contador = 1
    if i+1 < len(matriz) and matriz[i+1][j] == 1:
        matriz[i+1][j] = -1
        contador += tamanho_rio(matriz, i+1, j)
    if i > 0 and matriz[i-1][j] == 1:
        matriz[i-1][j] = -1
        contador += tamanho_rio(matriz, i-1, j)
    if j+1 < len(matriz[i]) and matriz[i][j+1] == 1:
        matriz[i][j+1] = -1
        contador += tamanho_rio(matriz, i, j+1)
    if j > 0 and matriz[i][j-1] == 1:
        matriz[i][j-1] = -1
        contador += tamanho_rio(matriz, i, j-1)    
    return contador

def identifica_rio(matriz):
    tamanho_dos_rios = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                matriz[i][j] = -1 
                tamanho_dos_rios.append(tamanho_rio(matriz, i, j))
    return tamanho_dos_rios

print()
print("Os tamanhos dos 'rios' identificados são:", identifica_rio(matriz.copy()))