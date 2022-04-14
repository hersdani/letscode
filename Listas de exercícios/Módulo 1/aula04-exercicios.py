'''
Questão #1
Crie uma lista qualquer e faça um programa que imprima cada elemento da lista usando o for.
'''

lista = [20, 100.0, "lista", 87.2, 29, "gato"]
for elemento in lista:
	print(elemento)

'''
Questão #2
Faça um programa que imprima todos os itens de uma lista usando while e compare com o exercício 1.
'''

lista = [20, 100.0, "lista", 87.2, 29, "gato"]
i = 0
tamanho = len(lista)
while i < tamanho:
    print(lista[i])
    i += 1

'''
Questão #3
Faça um programa que peça para o usuário digitar um número n e imprima uma lista com todos os números de 0 a n-1.

Exemplo: se o usuário digitar 5, o programa deve imprimir [0, 1, 2, 3, 4]
'''

numero = int(input('Digite um número: '))
for i in range(1, numero):
    print (i)

'''
Questão #4
Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
'''

# lista = [10, 11, 13, 20, 4, 2, 1, 100, "luz"]
lista = [10, 11, 13, 20, 4, 2, 1, 100]
contador = 0
inteiros = []
#for valor in lista:
#    if valor in lista != int(valor):
#        inteiros.append(int(valor))
    inteiros.append(int(valor))
for elemento in inteiros:
    sobra = elemento % 2
    if sobra == 0:
        contador += 1
print(contador)

'''
Questão #5
Faça um programa que imprima o maior número de uma lista, sem usar a função max().
'''

lista = [10, 11, 13, 20, 4, 2, 1, 100]
lista.sort(reverse = True)
print("O maior número da lista é: ", lista[0], "!")

x = int(input("Digite quantos números vão compor a lista: "))
lista = []
for i in range(0, x+1):
    n = int(input("Digite um número"))
    lista.append(n)
lista.sort(reverse = True)
print("O maior número da lista é: ", lista[0], "!")


'''
Questão #6
Enunciado
Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.

Dica: Use o método próprio de listas .remove().
'''

lista = [10, 1000, 200, 909, 3000, 2000, 45]
maximos = []
for valor in lista:
    maximo = max(lista)
    maximos.append(maximo)
    lista.remove(max(lista))
    if len(maximos) == 3:
         break
print(maximos)


lista = [10, 1000, 200, 909, 3000, 2000, 45]
maior = lista[0]
for elemento in lista:
	if elemento > maior:
		maior = elemento
print(maior)

'''
Questão #7
Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição.
Exemplo: Dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]
'''

#lista1 = [1, 4, 5]
#lista2 = [2, 2, 3]
#listasoma = []
#for n in lista1 and lista2:
#    soma = lista1[n] + lista2[n]
#    listasoma.append(lista1[n] + lista2[n])
#print(listasoma)

lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
listasoma = []
for n in lista1 and m in lista2:
    soma = lista1[n] + lista2[m]
    listasoma.append(lista1[n] + lista2[n])
print(listasoma)


lista1 = [1, 4, 5]
lista2 = [2, 2, 3]
listasoma = []
for n in range(len(lista1)):
    soma = lista1[n] + lista2[n]
    listasoma.append(soma)
print(listasoma)


'''
Questão #8
Faça um programa que pede para o usuário digitar 5 números e, ao final, imprime uma lista com os 5 números digitados pelo usuário (sem converter os números para int ou float).
Exemplo: Se o usuário digitar 1, 5, 2, 3, 6, o programa deve imprimir a lista ['1','5','2','3','6']
'''

lista = []
for n in range(5):
    x = str(input('Digite um número: '))
    lista.append(x)
print(lista)


'''
Questão #9
Pegue a lista gerada no exercício anterior e transforme cada um dos itens dessa lista em um float.
OBS: Não é para alterar o programa anterior, mas sim a lista gerada por ele.
'''

for n in range(5):
    lista[n] = (float(lista[n]))
print(lista)


'''
Questão #10
Faça um programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas.
'''

notas = []
# num_notas = int(input('Digite o numero de notas: '))
num_notas = 4
for i in range(num_notas):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
soma = 0
for elemento in notas:
    soma += elemento
media = soma / num_notas
print(media)

'''
Questão #11
Crie uma lista de 10 números e imprima:
a. uma lista com os 4 primeiros números;
b. uma lista com os 5 últimos números;
c. uma lista contendo apenas os elementos das posições pares;
d. uma lista contendo apenas os elementos das posições ímpares;
e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
f. uma lista inversa dos 5 primeiros números;
g. uma lista inversa dos 5 últimos números.
'''

lista = [10, 20, 15, 55, 100, 902, 28, 965, 77, 567]
listaa = []
for i in range(4):
    listaa.append(lista[i])
print('Os 4 primeiros números da lista:', listaa)
listab = []
for i in range(5, 10):
    listab.append(lista[i])
print('Os 5 últimos números da lista:', listab)

# pode fazer com slices tambem
lista = [10, 20, 15, 55, 100, 902, 28, 965, 77, 567]
listaa = lista[:4]
print('Os 4 primeiros números da lista:', listaa)
listab = lista[5:]
print('Os 5 últimos números da lista:', listab)
#

listac = []
tamanho = len(lista)
for i in range(1, tamanho, 2):
    listac.append(lista[i])
print("Os números nas posições pares são:", listac)
# ou
listac = lista[1:10:2]
print("Os números nas posições pares são:", listac)
# ou
#nao funciona ainda:
lista = [10, 20, 15, 55, 100, 902, 28, 965, 77, 567]
listac = []
tamanho = len(lista)
for i in range(1, tamanho, 2):
    if i%2 == 0:
        listac.append(lista[i])
print("Os números nas posições pares são:", listac)

listad = []
tamanho = len(lista)
for i in range(0, tamanho, 2):
    listad.append(lista[i])
print("Os números nas posições ímpares são:", listad)
# ou
listad = lista[0:10:2]
print("Os números nas posições ímpares são:", listad)

# posicões pares e ímpares, teria como fazer com operador resto?

lista = [10, 20, 15, 55, 100, 902, 28, 965, 77, 567]
listae = lista
listae.reverse()
print('A lista invertida é', listae)

lista = [10, 20, 15, 55, 100, 902, 28, 965, 77, 567]
listanova = lista
listanova.reverse()
listaf = listanova[:5]
print('Os 5 primeiros números da lista inversa:', listaf)

lista = [10, 20, 15, 55, 100, 902, 28, 965, 77, 567]
listanova = lista
listanova.reverse()
listag = listanova[5:]
print('Os 5 últimos números da lista inversa:', listag)


'''
Questão #12
Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
Obs.: Precisa usar a biblioteca random
'''

listaaleatorios = []
from random import randint
for n in range(10):
    numeroaleatorio = randint(1, 100) 
    listaaleatorios.append(numeroaleatorio)
contador = 0
for elemento in listaaleatorios:
	if elemento > 50:
		contador += 1
print('Os números sorteados foram', listaaleatorios, '.')
print('Dos números sorteados,', contador, 'são maiores que 50.')


'''
Questão #13
Faça um programa que sorteie 10 números entre 0 e 100 e imprima:
a. o maior número sorteado;
b. o menor número sorteado;
c. a média dos números sorteados;
d. a soma dos números sorteados.
Obs.: Precisa usar a biblioteca random
'''
listaaleatorios = []
from random import randint
for n in range(10):
    numeroaleatorio = randint(1, 100) 
    listaaleatorios.append(numeroaleatorio)
print('A lista dos dez números sorteados entre 0 e 100 é:', listaaleatorios, '.')
print('O maior número sorteado foi', max(listaaleatorios),'.')
print('O menor número sorteado foi', min(listaaleatorios),'.')
tamanho = len(listaaleatorios)
soma = 0
for i in listaaleatorios:
    soma += i
print('A média dos números sorteados é', soma/tamanho, '.')
print('A soma dos números sorteados é', soma, '.')




'''
desafio cpf
transformar o cpf em lista
como?
loop pra fazer uma operacao aritmetica q extrai o ultimo elemento, append numa lista, repete pra fazer
depois reverse
e faz a verificacao de cada elemento da lista
'''

'''
Questão #14
Super Desafio - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF pelos números de 10 a 2 e somar todas as respostas. O resultado deve ser multiplicado por 10 e dividido por 11. O resto dessa divisão deve ser igual ao primeiro dígito verificador (10º dígito). Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior para verificar o segundo dígito verificador.
Exemplo:
Se o CPF for 286.255.878-87 o programa deve fazer primeiro:
x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)
Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim, o programa deve calcular:
x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)
e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).
'''

CPF1 = str(input('Digite seu CPF sem pontos ou traço: '))
CPF2 = list(CPF1)
for n in range(len(CPF2)):
    CPF2[n] = int(CPF2[n])
x = 0
produto1 = 10
for i in range(1, len(CPF2)-1):
    x += CPF2[i-1]*(produto1)
    produto1 -= 1
validacao = x*10%11
if validacao == CPF2[9]:
    x = 0
    produto2 = 11
    for i in range(1, len(CPF2)):
        x += CPF2[i-1]*(produto2)
        produto2 -= 1
validacao = x*10%11 #teria como fazer sem colocar a variavel de novo?
    if validacao == CPF2[10]:
        print('CPF válido!')
    else:
        print('CPF inválido!')
else:
    print('CPF inválido!')