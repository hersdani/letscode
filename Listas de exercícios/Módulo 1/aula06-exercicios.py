
#1

import email


def dobro(num):
    x = 2 * num
    return x

valor = float(input('Digite um numero: '))
print('O dobro do numero é ', dobro(valor))

#2

def circunferencia(raio):
    c = 2 * 3.1415 * raio
    return c


r = float(input('Digite o raio:'))
print(circunferencia(r))


#3

def somar(num1, num2):
    soma = num1 + num2
    return soma

print(somar(50, 2))

def subtrair(num1, num2):
    subtrai = num1 - num2
    return subtrai

print(subtrair(50, 2))

def multiplicar(num1, num2):
    vezes = num1 * num2
    return vezes

print(multiplicar(4, 5))

def dividir(num1, num2):
    divisao = num1 / num2
    return divisao

print(dividir(50, 10))


#4

def printnome(nome):
    print('olá,', nome)

printnome(input('Digite um nome'))

#5

def saudacao(nome, hora):
    if 0 <= hora < 12:
        print('Bom dia,', nome)
    elif 12 <= hora < 18:
        print('Boa tarde,', nome)
    elif 18 <= hora < 24:
        print('Boa noite,', nome)
    else:
        print('Hora inválida,', nome)

saudacao(input("nome"), int(input('Digite a hora (24h)')))

#6

def par(num):
    return num % 2 == 0

print(par(22))


#7
def sorteia10():
    listaaleatorios = []
    from random import randint
    for n in range(10):
        numeroaleatorio = randint(1, 100) 
        listaaleatorios.append(numeroaleatorio)
    return max(listaaleatorios)

print(sorteia10())


#8

def sorteian(n):
    listaaleatorios = []
    from random import randint
    for i in range(n):
        numeroaleatorio = randint(1, 100) 
        listaaleatorios.append(numeroaleatorio)
    return sum(listaaleatorios) / len(listaaleatorios)

x = 2
print(sorteian(x))


#9
def maiusculas(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].upper()
    return lista

lista = ['Daniel', 'daniel', 'RAFAel', 'nome']
print(maiusculas(lista))

#10
def somalista(lista1, lista2):
    listasoma = []
    listastring = []
    for n in range(len(lista1)):
        soma = lista1[n] + lista2[n]
        listastring.append(str(lista1[n]) + '+' + str(lista2[n])) # como colocar o sinal de + entre os dois numeros na listastring?
        listasoma.append(soma)
    return listastring, listasoma 

lista1 = [1,4,3]
lista2 = [3,5,1]

resultado = somalista(lista1, lista2)
origem = resultado[0]
fim = resultado[1]
print(origem, '=', fim)
# ou 
origem, fim = somalista(lista1, lista2)
print(origem, '=', fim)

#11
def multlista(lista):
    listamult = []
    mult = 5
    for n in range(len(lista)):
        listamult.append(lista[n] * mult)
    return listamult

lista2 = [3,5,1]    
print(multlista(lista2))


#12
def produtolista(lista1, lista2):
    listaproduto = []
    for n in range(len(lista1)):
        produto = lista1[n] * lista2[n]
        listaproduto.append(produto)
    return listaproduto

lista1 = [1,4,3]
lista2 = [3,5,1]

print(produtolista(lista1, lista2))

#13
def somaitens(lista):
    soma = 0
    for n in range(len(lista)):
        soma += lista[n]
    return soma

lista = [3,5,1,1,10,80]
print(somaitens(lista))

#14
def mediaitens(lista):
    soma = 0
    for n in range(len(lista)):
        soma += lista[n]
        media = soma / len(lista)
    return media

lista1 = [1,4,3]
lista2 = [3,5,1]
print(mediaitens(lista2))


#15

def fatorial(num):
    produto = 1
    for n in range(num, 1, -1):
        produto *= n
    return produto

print(fatorial(6))

#16 

# -- nao funciona -----------------------------
def fibonacci(num):
    soma1 = 0
    for n in range(3, num-2):
        soma1 += soma1(n)
    #    print('soma1 é', soma1)
    soma2 = 0
    for i in range(3, num-1):
        soma2 += soma2(i)
    #    print('soma2 é', soma2)
#    soma = soma1 + soma2
#    print(soma)
    return soma1
# --------------------------------

def fibonacci(num):
    if (num==1) or (num==2):
        return 1
    else:
        ultimo=1
        penultimo=1
        for i in range(2,num):
            soma = ultimo + penultimo
#            print(ultimo,'+', penultimo, '=', soma)
            penultimo = ultimo
            ultimo = soma
            i += 1
        return soma

#forma alternativa (do Helldanio) - fórmula de BINET para cálculo de um determinado termo na sequência de Fibonacci.
def fibonacci(termo):
    resultado = (1.618034**termo)-(1-1.618034)**termo
    resultado = int(resultado/(5**0.5))
    return(resultado)

fibonacci(20)

# 17
def fatorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x * fatorial(x-1)
fatorial(5)

# 18

def verificadados(x, y):
    if y == 'idade':
        if x < 0 or x > 150:
            print('Erro: Idade inválida!')
        else:
            print('Idade OK:', x)
    elif y == 'salario':
        if x <= 0:
            print('Erro: Salário inválido!')
        else:
            print('Salário OK:', x)
    elif y == 'genero':
        if x.upper() != 'M' and x.upper() != 'F' and x.capitalize() != 'Outro':
            print('Erro: Gênero inválido!')
        else:
            print('Gênero OK: ', x.capitalize())

verificadados('f', 'genero')


#19

def fibonacci(x):
    if (x==1) or (x==2):
        return 1
    else:
        soma = fibonacci(x-1) + fibonacci(x-2)
        return soma

print(fibonacci(20))


#20


def baralho21 ():
    baralho = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

def jogada21():
    jogadores = {}
    for n in range (njog):
        nomejogador = input('Digite o nome do jogador: ')
        if nomejogador in jogadores:
            print(Erro! Nome já existe, digite outro nome!)
        else: 
            jogadores[nomejogador] = {'nome' = nomejogador, 'pontos' = 0}
    if 


def sorteio21():
#from random import random
    from random import choice
    carta = choice(baralho)
    if (carta == 'A') or (carta == 'J') or (carta == 'Q') or (carta == 'K'):
        if carta == 'A':
            ponto = 1
        else:
            ponto = 10
    else:
        ponto = carta
    return ponto


def verifica21():
    pass
    return


def principal21 ():
    njog = int(input('Digite o número de jogadores (>=1): '))
    baralho21()
    jogadores = {}
    for n in range (njog):
        nomejogador = input('Digite o nome do jogador: ')
        jogadores[n+1] = {'nome' : nomejogador, 'pontos' : 0, 'ativo' : 'S'}
#    if nomejogador in jogadores['nome']:
#        print('Erro! Nome já existe, digite outro nome!')
#    else: 
#        jogadores[n+1] = {'nome' : nomejogador, 'pontos' : 0}


# testes #
baralho = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
from random import choice
carta = choice(baralho)
njog = 3
jogadores = {}
repetido = False
for m in range(1, njog):
    nomejogador = input('Digite o nome do jogador: ')
    jogadores[m] = {'nome' : nomejogador, 'pontos' : 0, 'ativo' : 'S'}
    for n in range (1, njog):
        if jogadores[n]['nome'] == nomejogador:
            repetido = True
        if repetido == True:
            print('Erro! Nome já existe, digite outro nome!')
            jogadores[n] = {'nome' : nomejogador, 'pontos' : 0, 'ativo' : 'S'}
            break

        
         
# dicionario com ID (sequencial), nome, pontuação, status (ativo ou nao)
# como pesquisar no dicionario o nome pra saber se já tem?

print(jogadores)



$njog = 3
jogadores = {}
repetido = False
for m in range(1, njog):
    nomejogador = input('Digite o nome do jogador: ')
    jogadores[m] = {'nome' : nomejogador, 'pontos' : 0, 'ativo' : 'S'}
    for n in range (1, njog):
        if jogadores[n]['nome'] == nomejogador:
            repetido = True
        if repetido == True:
            print('Erro! Nome já existe, digite outro nome!')
            jogadores[n] = {'nome' : nomejogador, 'pontos' : 0, 'ativo' : 'S'}
            break


# 21

def cadastro():
    nome = input('Digite o nome: ')
    cpf = str(input('Digite o CPF: '))
    email = str(input('Digite o e-mail: '))
    clientescadastrados.append([nome, cpf, email])
    return clientescadastrados
def verifica(clientescadastrados, cpf):
    for elemento in range(len(clientescadastrados)):
        cliente = []
        if cpf in clientescadastrados[elemento][1]:
            cliente.append(clientescadastrados[elemento])
            break
        else:
            cliente = 'Cliente não cadastrado!'
            #break
    return cliente    
clientescadastrados = []
x = 1
while x != 0:
    x = int(input('Digite uma opção: \n [0] Sair \n [1] Cadastrar novo cliente \n [2] Pesquisar um cliente pelo CPF \n [3] Exibe todos os clientes cadastrados \n'))
    if x == 1:
         cadastro()
    elif x == 2:
        cpf = str(input('Digite o CPF: '))
        print(verifica(clientescadastrados, cpf))
    elif x == 3:
        print('Lista de todos os clientes cadastrados:', clientescadastrados)
    elif x < 0 or x >= 4:
        print('Opção inválida!')
print('Obrigado por usar o programa, volte sempre!')












