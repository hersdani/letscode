import json
import os.path
import sys

def obter_dados():
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    categorias = []
    for elemento in dados:
        if elemento['categoria'] in categorias: 
            continue
        else:
            categorias.append(elemento['categoria'])
    categoriasordenadas = sorted(categorias)
    return categoriasordenadas

def listar_por_categoria(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    produtos = []
    for elemento in dados:
        if categoria == elemento['categoria']:
            produtos.append({'id':elemento['id'], 'preco':elemento['preco']})
        else:
            continue
    return produtos

def produto_mais_caro(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    x = listar_por_categoria(dados, categoria)
    maiscaro = [ {'id':'0', 'preco': '0'}]
    for elemento in x:
        if float(elemento['preco']) > float(maiscaro[0]['preco']):
            maiscaro[0] = elemento
    for elemento in x:
        if elemento in maiscaro:
            continue
        elif float(elemento['preco']) == float(maiscaro[0]['preco']):
            maiscaro.append(elemento)
    return maiscaro[0]

def produto_mais_barato(dados, categoria):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    x = listar_por_categoria(dados, categoria)
    maisbarato = [ produto_mais_caro(dados, categoria)]
    for elemento in x:
        if float(elemento['preco']) < float(maisbarato[0]['preco']):
            maisbarato[0] = elemento
    for elemento in x:
        if elemento in maisbarato:
            continue
        elif float(elemento['preco']) == float(maisbarato[0]['preco']):
            maisbarato.append(elemento)
    return maisbarato[0]

def top_10_caros(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    # A primeira ideia que tive para essa função foi pegar os valores da chave
    # 'preco' em dados, colocar em uma lista, ordenar, pegar os 10 maiores e 
    # depois pegar cada valor, procurar por ele em dados e colocar o elemento 
    # em uma nova lista. Mas pensei que poderia dar problema se houvesse dois
    # preços iguais, pois ao percorrer a lista ia encontrar o mesmo preço na primeira
    # vez e colocar o mesmo produto duas vez. 
    # Então fiz de uma outra forma nesta função top_10_caros. Tive muito trabalho pq 
    # não sabia que listanova = listaantiga apontava para o mesmo lugar da memória
    # (cada vez que rodava, descartava os 10 mais caros, p.ex, primeiro mostrava do
    # 1 ao 10, depois do 11 ao 20 e assim por diante).
    # Tive que pesquisar no Google para descobrir listanova = lista[:]. Não
    # lembro se foi dado em aula.
    # Depois de começar a fazer da forma abaixo, pensei em um jeito de evitar
    # problemas com produtos de precos diferentes que citei. 
    # Usei a outra forma na função top_10_baratos.
    dadostemp = dados[:]
    os10maiscaros = []
    while len(os10maiscaros) != 10:
        maiscarostemp = [ {'id':'0', 'preco': '0', 'categoria': 'nenhuma'}]
        for elemento in dadostemp:
            if float(elemento['preco']) >= float(maiscarostemp[0]['preco']):
                maiscarostemp[0] = elemento
        dadostemp.remove(maiscarostemp[0])
        os10maiscaros.append(maiscarostemp[0])
    return os10maiscaros

def top_10_baratos(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    soprecos = []
    os10maisbaratos = []
    for elemento in dados:
        soprecos.append(float(elemento['preco']))
    soprecos.sort()
    precos10 = soprecos[:10]
    for contador in range(len(precos10)):
        for elemento in dados:
            if elemento in os10maisbaratos:
                continue
            elif float(elemento['preco']) == float(precos10[contador]):
                os10maisbaratos.append(elemento)
    return os10maisbaratos

def menu(dados):
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
        1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    # pedir Produto mais caro por categoria (ou mais barato) pode parecer que quer o produto
    # de *cada* categoria.
    opcao = 1
    while opcao != 0:
        opcao = input('Digite uma das opções abaixo:\n1. Listar categorias\n2. Listar produtos de uma categoria\n3. Produto mais caro por categoria\n4. Produto mais barato por categoria\n5. Top 10 produtos mais caros\n6. Top 10 produtos mais baratos\n0. Sair')
        if opcao.isdigit() == False:
            print('Opção inválida! Escolha uma opção ente 0 e 6!')
        else:
            opcao =int(opcao) 
            if opcao == 1:
                categoria1 = listar_categorias(dados)
                print('Lista de categorias:')
                for elemento in categoria1:
                    print(elemento)
            elif opcao == 2:
                categoria2 = input('Digite a categoria que deseja listar os produtos: \n(ou digite 9 para voltar)')
                z = listar_categorias(dados)
                if categoria2 == '9':
                    menu(dados)
                else:
                    while categoria2 not in z:
                            print('Categoria não existe!')
                            categoria2 = input('Digite uma outra categoria: ')
                    produtos_cat = listar_por_categoria(dados, categoria2)
                    print('Lista de produtos - categoria', categoria2)
                    for elemento in produtos_cat:
                        print('id:', elemento['id'],'- preço:', elemento['preco'])
            elif opcao == 3:
                categoria3 = input('Digite a categoria que deseja exibir o produto mais caro: \n(ou digite 9 para voltar)')
                z = listar_categorias(dados)
                if categoria3 == '9':
                    menu(dados)
                else:
                    while categoria3 not in z:
                            print('Categoria não existe!')
                            categoria3 = input('Digite uma outra categoria: ')
                    produto_mais_caro_cat = produto_mais_caro(dados, categoria3)
                    print('O produto mais caro da categoria', categoria3, 'é:\n ', 'id:', produto_mais_caro_cat['id'], '- preco:', produto_mais_caro_cat['preco'])
            elif opcao == 4:
                categoria4 = input('Digite a categoria que deseja exibir o produto mais barato: \n(ou digite 9 para voltar) ')
                z = listar_categorias(dados)
                if categoria4 == '9':
                    menu(dados)
                else:
                    while categoria4 not in z:
                            print('Categoria não existe!')
                            categoria4 = input('Digite uma outra categoria: ')
                    produto_mais_barato_cat = produto_mais_barato(dados, categoria4)
                    print('O produto mais barato da categoria', categoria4, 'é:\n ', 'id:', produto_mais_barato_cat['id'], '- preco:', produto_mais_barato_cat['preco'])
            elif opcao == 5:
                top10maiscaros = top_10_caros(dados)
                print('Lista dos dez produtos mais caros:')
                for elemento in top10maiscaros:
                    print('id:', elemento['id'], '- preco:', elemento['preco'], '- categoria:', elemento['categoria'])
            elif opcao == 6:
                top10maisbaratos = top_10_baratos(dados)
                print('Lista dos dez produtos mais baratos:')
                for elemento in top10maisbaratos:
                    print('id:', elemento['id'], '- preco:', elemento['preco'], '- categoria:', elemento['categoria'])
            elif opcao < 0 or opcao > 6:
                print('Opção inválida! Escolha uma opção ente 0 e 6!')
    print('Obrigado por usar o programa, volte sempre!')   


# Programa Principal - não modificar!
d = obter_dados()
print('Olá! Sistema de retaguarda do Magalu. Bem vindo!')
menu(d)