
# exercícios while e for

#1

numero = int(input('Digite um número: '))
i = 1
while i <= numero:
    print (i)
    i += 1

numero = int(input('Digite um número: '))
for i in range(1, numero+1):
    print (i)

#2
numero = int(input("Digite um número: ") )
resultado = 1
i = 1
while i <= numero:
    resultado *= i
    i += 1
print('O fatorial de', numero, 'é:', resultado)

numero = int(input("Digite um número: ") )
resultado = 1
for i in range(1, numero+1):
    resultado *= i
print('O fatorial de', numero, 'é:', resultado)

#3
numero = int(input("Digite um número: ") )
soma = 0
i = 1
while i <= numero:
    soma = soma + i
    i += 1
print('A soma de cada número de 1 até', numero, 'é:', soma)

numero = int(input("Digite um número: ") )
soma = 0
for i in range(1, numero+1):
    soma += i
print('A soma de cada número de 1 até', numero, 'é:', soma)

#4
numero = 9
i = 1
while i <= numero + 1:
    print(numero,'*',i,'=', numero*i) 
    i += 1

numero = 9
for i in range(1, numero+2):
    print(numero,'*',i,'=', numero*i) 

#5
numero = 1
soma = 0
while numero != 0:
    numero = int(input('Digite um número (digite 0 para sair e somar): '))
    soma = soma + numero
print ('A soma dos números digitados é:', soma)

numero = 0
from random import randint
aleatorio = randint(1, 100)
print(aleatorio)
while numero != aleatorio:
    numero = int(input('Adivinhe o número (entre 1 e 100): '))
    if numero != aleatorio:
        print('Você errou! Digite um novo número')
print('Parabéns, você acertou o número!')

#6
idade = int(input('Digite uma idade entre 0 e 150: '))
while idade < 0 or idade > 150:
    print('Erro: Idade inválida!')
    idade = int(input('Digite outra idade: '))
print('Idade OK:', idade)
salario = float(input('Digite um salário maior que 0: '))
while salario < 0:
    print('Erro: Salário inválido!')
    salario = float(input('Digite outro salário: '))
print('Salário OK:', salario)
genero = input('Digite o gênero (M, F ou Outro): ')
while genero != 'M' and genero != 'F' and genero != 'Outro':
    print('Erro: Gênero inválido!')
    genero = input('Digite outro gênero: ')
print('Gênero OK: ', genero)

###### 7

i = 0 
soma = 0 
termo = 1 
while i < 1000: 
    soma = soma + termo 
    termo = termo / 2 
    i += 1 
print(soma)

termo = 1
soma = 0
for i in range(0,1000+1):
    soma += termo
    termo = termo / 2
print(soma)



### 8
i = 1
soma = 0
fatorial = 1
while i <= 1000:
    termo = 1 / fatorial
    soma = soma + termo
    fatorial *= i
    i += 1
print(soma)

# resposta 1.718

fatorial = 1
soma = 0
for i in range(1,1000+1):
    termo = 1 / fatorial
    soma += termo
    fatorial *= i
    #print (f'({i}!) = {fatorial} -> {soma}')
print(soma)



# desafio, refazer o exercicio 6 com aviso dizendo se o chute estava acima ou abaixo, e contar as tentativas