
#1
Mes_Dias = {
    'Janeiro':31, 
    'Fevereiro':28, 
    'Março':31, 
    'Abril':30, 
    'Maio':31, 
    'Junho':30, 
    'Julho':31, 
    'Agosto':31, 
    'Setembro':30, 
    'Outubro':31, 
    'Novembro':30, 
    'Dezembro':31}
print(Mes_Dias)

#2
for chave in Mes_Dias:
    print(chave, '-', Mes_Dias[chave])

#3
dicionario = {'Banana': 3.0, 'Cebola': 4.0, 'Maçã': 5.7, 'Abacaxi': 8.0}
print(dicionario)

#4
dicionario.update({'Maçã':'8.6'})

#5
def gravadados(nome, idade, email):
     return { "nome": nome, "idade": idade, "email": email }

nome = 'João'
idade = 80
email = 'meuemail@provedor.com'

print(gravadados(nome,idade, email))

#6
#dicionario = {'Nome': ['Maria', 'Pedro', 'João'], 
#              'Coluna A': [1, 0.5, 3.2], 
#              'Coluna B': [5, 3, 1]}
#print(dicionario)
dicionario = {'Maria' : {'Coluna A' : 1,
                       'Coluna B' : 5},
              'Pedro' : {'Coluna A' : 0.5,
                       'Coluna B' : 3},
              'João' : {'Coluna A' : 3.2,
                       'Coluna B' : 1}}
print(dicionario['Pedro']['Coluna B'])

#7
#lista1 = [3, 4, 50, 20, 50, 4, 4, 1, 600, 200, 'Rafael', 'Daniel', 'Rafael', 'Michel']
#lista2 = []
#for elemento in lista1:
    #if elemento in lista2:
    #    contador += 1
    #    print(contador)
    #else:
    #    lista2.append(elemento)
    # print(contador)
lista = [3, 4, 50, 20, 50, 4, 4, 1, 600, 200, 'Rafael', 'Daniel', 'Rafael', 'Michel']
dicionario = {}
for i in range(len(lista)):
    repeticoes = lista.count(lista[i])
    dicionario.update({lista[i] : repeticoes})
print(dicionario)
    
#8

r = 1
dicionario = {}
while r != 3:
    r = int(input('Digite uma opcão: \n 1: Cadastrar novo usuário \n 2: Listar usuários cadastrados\n 3: Fechar o programa'))
    if r == 1:
        cpf = input('Digite o CPF sem pontos ou traço: ')
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        email = input('Digite o email: ')
        dicionario[cpf] = {'nome': nome, 'idade': idade, 'email': email}
    elif r == 2:
        print(dicionario)
print('Obrigado por usar o programa, volte sempre!')    

# metodo com update e com colchetes?


#9?
r = 1
dicionario = {}
while r != 3:
    r = int(input('Digite uma opcão: \n 1: Cadastrar novo usuário \n 2: Listar usuários cadastrados\n 3: Fechar o programa \n 4: Buscar CPF' ))
    if r == 1:
        cpf = input('Digite o CPF sem pontos ou traço:')
        nome = input('Digite o nome:')
        idade = input('Digite a idade:')
        email = input('Digite o email:')
        dicionario[cpf] = {'nome': nome, 'idade': idade, 'email': email}
    elif r == 2:
        print(dicionario)
    elif r == 4:
        buscaCPF = input("Digite o CPF para buscar: ") 
        if buscaCPF in dicionario:
            print(dicionario[buscaCPF])
        else:
            print("Esse CPF não está cadastrado!")
    elif r <= 0 or r > 4: 
        print('Opção inválida!')
print(dicionario)
print('Obrigado por usar o programa, volte sempre!')    
