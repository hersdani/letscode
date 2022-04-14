
grafo = [
    [1,2],
    [0],
    [0],
    [4,5],
    [3,5],
    [3,4]
]
# grafo1
# tem que ter mais duas entradas
# ver se existe o caminho
# depois identificar o caminho

def dfs(grafo, vertice_inicial, vertice_final, visitados = list()):
    visitados.append(vertice_inicial)
    print(vertice_inicial)
    for vizinho in grafo[vertice_inicial]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
    
    return visitados
    
print(dfs(grafo, 0, 5))
