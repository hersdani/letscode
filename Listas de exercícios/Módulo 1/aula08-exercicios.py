'''
Questão #1
Faça um programa que peça para o usuário digitar uma palavra e imprima cada letra em uma linha.
'''
palavra = input('Digite uma palavra:')
for l in palavra:
    print (l)


'''
Questão #2
Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, copiando letra por letra a palavra digitada, depois imprima a nova string.
'''
palavra1 = input('Digite uma palavra:')
listapalavra = list(palavra1)
print(listapalavra)
palavra2 = ''
for letra in listapalavra:
    palavra2 = palavra2 + letra
print(palavra2)

# outra forma:
palavra1 = input('Digite uma palavra:')
listapalavra = list(palavra1)
palavra2 = ''.join(listapalavra)
print(palavra2)

'''
Questão #3
Altere o exercício anterior para que a string copiada alterne entre letras maiúsculas e minúsculas.
Exemplo: se o usuário digitar "latex" o programa deve imprimir "LaTeX".
'''
# nao funcionou
palavra1 = input('Digite uma palavra:')
listapalavra = list(palavra1)
palavra2 = ''
maiuscula = True
for letra in range(len(listapalavra)):
    if maiuscula == False:
        palavra2 = palavra2 + listapalavra[letra].lower()
        maiuscula = True
    elif maiuscula == False:
        palavra2 = palavra2 + listapalavra[letra].upper()
        maiuscula = True
        continue
print(palavra2)

# funcionou
palavra1 = input('Digite uma palavra:')
listapalavra = list(palavra1)
palavra2 = ''
maiuscula = True
for letra in listapalavra:
    if maiuscula == True:
        palavra2 = palavra2 + letra.upper()
        maiuscula = False
        continue
    elif maiuscula == False:
        palavra2 = palavra2 + letra.lower()
        maiuscula = True
print(palavra2)

'''
Questão #4
Faça um programa que pede para o usuário digitar uma palavra e cria uma nova string igual, porém com espaço entre cada letra, depois imprima a nova string:
Exemplo: se o usuário digitar "python" o programa deve imprimir "p y t h o n "
'''
palavra1 = input('Digite uma palavra:')
listapalavra = list(palavra1)
palavra2 = ''
for letra in listapalavra:
    palavra2 = palavra2 + letra + ' '
print(palavra2)


'''
Questão #5
Faça uma função que receba uma string e retorne uma nova string substituindo:
'a' por '4'
'e' por '3'
'I' por '1'
't' por '7'
'''

#nao funciona
palavra1 = input('Digite uma palavra:')
palavra2 = ''
for i in range(len(palavra1)):
    palavra2 = palavra1[i].replace('a', '4')
    palavra2 = palavra1[i].replace('e', '3')
    palavra2 = palavra1[i].replace('I', '1')
    palavra2 = palavra1[i].replace('t', '7')
print(palavra2)

#funciona
palavra1 = input('Digite uma palavra:')
palavra2 = ''
for letra in palavra1:
    palavra2 = palavra1.replace('a', '4')
    palavra2 = palavra2.replace('e', '3')
    palavra2 = palavra2.replace('I', '1')
    palavra2 = palavra2.replace('t', '7')
print(palavra2)
#

#funciona
def alteraletras(palavra1):
    substituido1 = palavra1.replace('a', '4')
    substituido1 = substituido1.replace('e', '3')
    substituido1 = substituido1.replace('I', '1')
    substituido1 = substituido1.replace('t', '7')
    return(substituido1)
print(alteraletras(palavra1))


'''
Questão #6
Faça uma função que recebe uma string e retorna ela ao contrário.
Exemplo: Recebe "teste" e retorna "etset".
'''

def inverte(palavra):
    return palavra[::-1]

print(inverte('Daniel'))

'''
Questão #7
Agora faça uma função que recebe uma palavra e diz se ela é um palíndromo, ou seja, se ela é igual a ela mesma ao contrário.
Dica: Use a função do exercício 6.
'''
def palindrona(palavra):
    if palavra == palavra[::-1]:
        return 'A palavra é palíndroma'
    else:
        return 'A palavra não é palíndroma'

print(palindrona('asas'))


'''
Questão #8
Faça uma função que receba um texto e uma palavra, então verifique se a palavra está no texto, retornando True ou False.
'''

def contempalavra(texto, palavra):
    textoseparado = texto.split()
    if palavra in textoseparado:
        return True
    else:
        return False

print(contempalavra("O rato tem dois dedos", "rat"))

'''
Questão #9
Faça uma função que receba uma string que contém tanto números quanto letras e caracteres especiais, e que separe as letras em uma variável e os números em outra (os caracteres especiais podem ser descartados). Ao final a função deve imprimir as duas variáveis.
'''
#nao funciona
def separa(texto):
    lista = list(texto)
    numeros = []
    letras = []
    for elemento in lista:
        if elemento == int(elemento):
            numeros.append(elemento)
        elif elemento == str(elemento):
            letras.append(elemento)
    return letras, numeros

#funciona
def separa(texto):
    lista = list(texto)
    numeros = []
    letras = []
    for elemento in lista:
        if elemento.isalpha():
            letras.append(elemento)
        elif elemento.isdecimal():
            numeros.append(elemento)
        else:
            continue
    return ''.join(letras), ''.join(numeros)

print(separa('oks902ue328ejwd@&#&*#'))

'''
Questão #10
Desafio - Faça uma função que receba uma string e uma letra e:
a. imprima quantas vezes a letra aparece na string;
b. imprima todas as posições em que a letra aparece na string;
c. retorne a distância entre a primeira e a última aparição dessa letra na string.
'''

def contastr(texto, letra):
    contador = 0
    posicaoletra = []
    for i in range(len(texto)):
        if letra == texto[i]:
            contador += 1
            posicaoletra.append(i)
        else:
            continue
    distancia = posicaoletra[-1] - posicaoletra[0]
    return contador, posicaoletra, distancia

texto = 'abchabcdhabchabdcsa'
letra = 'h'
print(contastr(texto, letra))


'''
Questão #11
Super Desafio! - faça uma função que criptografa uma mensagem substituindo cada letra pela letra oposta do dicionário:
'a' por 'z'
'b' por 'y'
'c' por 'x'
...
'''


def criptografa(mensagem):
    mensagemcripto = ''
    letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letras_minusculas = letras_maiusculas.lower()
    # mensagem_maiuscula = mensagem.upper()
    for i in range(len(mensagem)):
        if mensagem[i] in letras_maiusculas:
            for j in range(len(letras_maiusculas)):
                mensagem[i] = letras_maiusculas[(len(letras_maiusculas)-(j+1))]
                mensagemcripto = mensagemcripto + mensagem[i]
        elif mensagem[i] in letras_minusculas:
            for k in range(len(letras_maiusculas)):
                mensagem[i] = letras_maiusculas[len(letras_maiusculas)-(k+1)]
                mensagemcripto = mensagemcripto + mensagem[i]
        else:
            continue
    return mensagemcripto

# mensagemp[n] = mensagem[::-1]
mensagem = 'Hoje tem aula de Python'
print(criptografa(mensagem))

mensagem = 'Olá amigo, você é um amigo!'


    #for i in range(len(mensagem)):
