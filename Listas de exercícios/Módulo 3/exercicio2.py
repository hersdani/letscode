class NoArvore:
    def __init__(self, valor=0, nosFilhos=list()):
        self.valor = valor
        self.nosFilhos = nosFilhos

def busca_filhos(_nos,posicao):    
    if len(_nos[posicao].nosFilhos) > 0 and _nos[posicao].valor != ultimo_no:
        return busca_filhos(_nos,posicao+1)
    else:
        return 1

nos = []
nos.append(NoArvore(3,[9,20]))
nos.append(NoArvore(9))
nos.append(NoArvore(20,[15,7]))
nos.append(NoArvore(15))
nos.append(NoArvore(7))

# Considerando a árvore binária, o sistema vai percorrer os nós e a cada 3 nós diminuirá a contagem em 1
# levando-se em conta que pode haver uma ramificação e outros nós abaixo, caso seja o último nó consultado
# "x < len(nos)-1"  a diminuição em 1 não ocorrerá pois a varredura estará completa.
ultimo_no = nos[len(nos)-1].valor
tamanho = 0
for x in range(len(nos)):
    tamanho += busca_filhos(nos,x)
    if tamanho%3 == 0 and x < len(nos)-1:
        tamanho -= 1
print(tamanho)
