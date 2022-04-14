
# fazer tratamento de excecoes com raide e/ou try/except

# tirar o atributos numero_bicicletas_alugadas, modo_aluguel, duracao do construtor do cliente e colocar em outro metodo
# tipo def alugar_bicicletas:

# fiquei na duvida se colocava as saidas com print ou com return. mas aí dependeria se teria que fazer o programa inteiro ou só as classes

class Cliente:
    def __init__(self, nome, numero_bicicletas_alugadas, modo_aluguel, duracao):
        self.nome = nome
        self.numero_bicicletas_alugadas = numero_bicicletas_alugadas
        self.modo_aluguel = modo_aluguel
        self.duracao = duracao
        # pensar depois numa forma de fazer q no futuro trabalhe com cadastro de clientes separado, 
        # talvez numa outra classe ou arquivo com tabela ou dicionario.
        if self.numero_bicicletas_alugadas <= 0:
            print('Não é possível alugar zero ou um número negativo de bicicletas')
        # else:    
        #     # tratar outros possíveis erros nos atributos do construtor
        #     # (modo de aluguel só pode ser "hora", "dia", "semana")
        #     self.numero_bicicletas_alugadas = numero_bicicletas_alugadas
        if modo_aluguel.lower() != 'hora' and modo_aluguel.lower() != 'dia' and modo_aluguel.lower() != 'semana':
            print('Só é possível alugar por hora, dia ou semana!')
        # else:
        #     self.modo_aluguel = modo_aluguel
        #(duração > 0 - colocar um limite? hora < 24h, dia < 7, semana xxx?)
        if (modo_aluguel == 'hora' and duracao >= 24) or (modo_aluguel == 'dia' and duracao >= 7) or (duracao <= 0):
            if modo_aluguel == 'hora':
                print('Não é possível alugar mais que 24 horas seguidas. Escolha o aluguel por dia.')
            if modo_aluguel == 'dia':
                print('Não é possível alugar mais que 7 dias seguidos. Escolha o aluguel por semana.')
            elif duracao <= 0:
                print('Nao é possível alugar com um duração de zero ou um número negativo!')
            # else:
            #     self.duracao = duracao 
        # comecar fazendo com duracao previa, mas pensar no futuro em usar o datetime pra registrar o momento do aluguel 
        # e na loja registrar o momento de devolucao pra calcular o valor do aluguel

    def ver_estoque(self, loja):
        loja.mostrar_estoque()

class Loja:
    estoque_padrao = [{'id': 'Bike1', 'cor': 'vermelha', 'estoque': 8 },
             {'id': 'Bike2', 'cor': 'azul', 'estoque': 7},
             {'id': 'Bike3', 'cor': 'preta', 'estoque': 9},
             {'id': 'Bike4', 'cor': 'amarela', 'estoque': 6},
             {'id': 'Bike4', 'cor': 'preta', 'estoque': 10 }]
    def __init__(self, loja, estoque=estoque_padrao):
        # fazendo com atributo estoque padrão fora do contrutor é possivel colocar um estoque padrão para cada loja, mas alterar caso queira
        # depois pensar na possibilidade de fazer uma classe de bicicletas para entrada de estoque e saída de estoque, com a Loja chamando esta classe
        self.nomeloja = loja
        self.estoque = estoque
        total = 0
        for elemento in self.estoque:
            total += elemento['estoque']
        self.total_de_bicicletas = total
    
    # métodos:

    # receber pedidos de aluguel de cada tipo, validando a possibilidade
    # com o estoque e modo de aluguel existente

    def recebe_aluguel(self, cliente):
        bikes_alugadas = cliente.numero_bicicletas_alugadas
        print("Número de bicicletas atualmente disponíveis:", self.total_de_bicicletas)
        print("Bikes alugadas pelo cliente:", bikes_alugadas)
        if (bikes_alugadas) > (self.total_de_bicicletas):
            print("Não há bicicletas suficientes para este aluguel!")
            # print(self.estoque[0]['id'])
        # elif (bikes_alugadas) <= (self.total_de_bicicletas):
        else:
            for i in self.estoque:
                if bikes_alugadas == 0:
                    break
                if i['estoque'] == 0:
                    continue
                elif (i['estoque'] > 0):
                    if (i['estoque'] < bikes_alugadas):
                        bikes_alugadas = bikes_alugadas - i['estoque']
                        i['estoque'] -= i['estoque']
                    elif i['estoque'] >= bikes_alugadas:
                        i['estoque'] -= bikes_alugadas
                        bikes_alugadas = 0

            #será que tem como usar algo do construtor pra calcular o estoque? ou colocar esse for separado em outro metodo?
            self.total_de_bicicletas = 0
            for k in self.estoque:
                self.total_de_bicicletas += k['estoque']     
            print("Número de bicicletas disponíveis após o aluguel:", self.total_de_bicicletas)

        # com datetime receber o momento da devolucao e fazer a conta com o inicio do aluguel
        # pass

    def calcular_valor(self, cliente):
        self.cliente = cliente
        # valor por tipo de aluguel (hora, dia, semana)
        h = 5
        d = 25
        s = 100
        valor = cliente.duracao * self.cliente.numero_bicicletas_alugadas
        if (cliente.numero_bicicletas_alugadas) >= 3:
            desconto = 30 / 100
            if cliente.modo_aluguel == 'hora':
                preco_final = (valor * h)
            elif cliente.modo_aluguel == 'dia':
                preco_final = (valor * d)
            elif cliente.modo_aluguel == 'semana':
                preco_final = (valor * s)
            # print('O valor a ser pago pelo', self.cliente, 'por um aluguel de', cliente.numero_bicicletas_alugadas, 'bicicleta(s) por', cliente.duracao, cliente.modo_aluguel,'(s) é: R$', preco_final)
            # print(f"{'O valor a ser pago pelo(a) '}{cliente.nome}{' por um aluguel de '}{cliente.numero_bicicletas_alugadas}{' bicicleta(s) por '}{cliente.duracao}{' '}{cliente.modo_aluguel}{'(s) é: '}{'R$'}{preco_final:2f}")
            print(f"O valor a ser pago pelo(a) {cliente.nome} por um aluguel de {cliente.numero_bicicletas_alugadas} bicicleta(s) por {cliente.duracao} {cliente.modo_aluguel}(s) é: R${preco_final*(1-desconto):.2f}")
        else:
            if cliente.modo_aluguel == 'hora':
                preco_final = (valor * h)
            elif cliente.modo_aluguel == 'dia':
                preco_final = (valor * d)
            elif cliente.modo_aluguel == 'semana':
                preco_final = (valor * s)
            print(f"O valor a ser pago pelo(a) {cliente.nome} por um aluguel de {cliente.numero_bicicletas_alugadas} bicicleta(s) por {cliente.duracao} {cliente.modo_aluguel}(s) é: R${preco_final:.2f}")
    
    def mostrar_estoque(self):
        print('-----------------------------------------------------')
        print(f"{'  '}{'Modelo':<15s}|{'     '}{'Cor':<15s}|{'    '}{'Estoque':>10s}")
        print('-----------------------------------------------------')
        for elemento in self.estoque:
            print(f"{'  '}{elemento['id']:<15s}|{'     '}{elemento['cor']:<15s}|{'    '}{elemento['estoque']:>10d}")
        print('-----------------------------------------------------')
        print('A loja tem', self.total_de_bicicletas, 'bicicletas disponíveis para locação.')
        print('-----------------------------------------------------')
        #print(loja.estoque)

# ----------------------------------------------------------------

loja1 = Loja('Matriz')
# print(loja1.total_de_bicicletas)
# print(loja1.estoque)

estoque2 = [{'id': 'Bike1', 'cor': 'vermelha', 'estoque': 2 },
             {'id': 'Bike2', 'cor': 'azul', 'estoque': 12},
             {'id': 'Bike4', 'cor': 'preta', 'estoque': 9},
             {'id': 'Bike5', 'cor': 'amarela', 'estoque': 6},
             {'id': 'Bike9', 'cor': 'preta', 'estoque': 11 },
             {'id': 'Bike9', 'cor': 'azul', 'estoque': 10 }]
loja2 = Loja('Filial1', estoque2)
# print(loja2.total_de_bicicletas)
# print(loja2.estoque)

cliente1 = Cliente('John', 50, 'dia', 3)

cliente2 = Cliente('João', 3, 'hora', 5)

cliente3 = Cliente('Danielle', 2, 'semana', 2)

# cliente4 = Cliente('Michael', 1, 'hora', 50)
# cliente5 = Cliente('Dwight', 1, 'dia', 10)
# cliente6 = Cliente('Pike', 1, 'semana', 10)


# print(cliente1.nome, cliente1.numero_bicicletas_alugadas, cliente1.modo_aluguel, cliente1.duracao)



# loja1(cliente2) # funcionava e parou, pq?

loja1.recebe_aluguel(cliente1)

loja1.recebe_aluguel(cliente2)

# print(loja1.total_de_bicicletas)
# print(loja1.estoque)
# print(cliente2.nome, cliente2.numero_bicicletas_alugadas, cliente2.modo_aluguel, cliente2.duracao)


loja1.recebe_aluguel(cliente3)

cliente1.ver_estoque(loja1)
cliente3.ver_estoque(loja2)

#loja2.recebe_aluguel(cliente4)
# print(loja2.estoque)

loja1.calcular_valor(cliente3)
