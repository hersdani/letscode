
# fazer tratamento de excecoes com raide e/ou try/except

# fiquei na duvida se colocava as saidas com print ou com return. mas aí dependeria se teria que fazer o programa inteiro usando a saída dos metodos (aí usaria return)
# ou só as classes e metodos como algo inicial em fases de testes.

class Cliente:

    def __init__(self, nome, cpf, email=None):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        numero_bicicletas_alugadas = 0
        self.numero_bicicletas_alugadas = numero_bicicletas_alugadas
        # cadastra cada cliente em uma lista de clientes para todas as lojas (cadastro unificado de clientes)
        if len(Loja.clientes) == 0:
            Loja.clientes.append({'cpf':self.cpf, 'nome':self.nome, 'email':self.email})
        else:
            for i in range(len(Loja.clientes)):
                if self.cpf in Loja.clientes[i]['cpf']:
                    print('Cliente já cadastrado!')
                    break
            else:
                Loja.clientes.append({'cpf':self.cpf, 'nome':self.nome, 'email':self.email})
                    
    
    # cada cliente pode fazer um aluguel por vez. caso haja mais de um aluguel
    # o estoque da loja vai ser alterado, mas na hora de calcular o valor do aluguel
    # só vai usar os dados do último aluguel daquele cliente.
    # Uma opção seria gravar os dados da locação numa tabela, e na hora de calcular o
    # valor devolver as bicicletas para o estoque. Ou ainda permitir colocar um verificador
    # para não permitir um segundo aluguel do mesmo cliente (talvez criando um cadastro
    # de clientes com ID único e verificando se tem aluguel ativo ou nao)

    def alugar_bicicleta(self, numero_bicicletas_alugadas, modo_aluguel, duracao, loja):
        self.numero_bicicletas_alugadas = numero_bicicletas_alugadas
        self.modo_aluguel = modo_aluguel
        self.duracao = duracao
        loja.recebe_aluguel(self.cpf, numero_bicicletas_alugadas, modo_aluguel, duracao)

        # pensar depois numa forma de fazer q no futuro trabalhe com cadastro de clientes separado, 
        # talvez numa outra classe ou arquivo com tabela ou dicionario.

    def ver_estoque(self, loja):
        loja.mostrar_estoque()


class Loja:

    estoque_padrao = [
            {'id': 'Bike1', 'cor': 'vermelha', 'estoque': 8 },
            {'id': 'Bike2', 'cor': 'azul', 'estoque': 7},
            {'id': 'Bike3', 'cor': 'preta', 'estoque': 9},
            {'id': 'Bike4', 'cor': 'amarela', 'estoque': 6},
            {'id': 'Bike4', 'cor': 'preta', 'estoque': 10 }]
    
    clientes = []

    def __init__(self, loja, estoque=estoque_padrao):
        # fazendo com atributo estoque padrão fora do contrutor é possivel colocar um estoque padrão para cada loja, mas alterar caso queira
        # depois pensar na possibilidade de fazer uma classe de bicicletas para entrada de estoque e saída de estoque, com a Loja chamando esta classe
        self.nomeloja = loja
        self.estoque = estoque
        total = 0
        alugueis_ativos = []
        self.alugueis_ativos = alugueis_ativos        
        for elemento in self.estoque:
            total += elemento['estoque']
        self.total_de_bicicletas = total
    
    def recebe_aluguel(self, cpf, numero_bicicletas_alugadas, modo_aluguel, duracao): 

        cpf_com_aluguel = 0
        if len(self.alugueis_ativos) > 0: 
            for elemento in self.alugueis_ativos:
                if cpf == elemento['cpf']:
                    cpf_com_aluguel = 1
                    break
        if cpf_com_aluguel == 1:
            print('Cliente com aluguel ativo, não pode fazer um novo aluguel!')
        elif cpf_com_aluguel == 0:
            self.modo_aluguel = modo_aluguel
            if numero_bicicletas_alugadas <= 0:
                print('Não é possível alugar zero ou um número negativo de bicicletas')
            elif numero_bicicletas_alugadas > self.total_de_bicicletas:
                print("Não há bicicletas suficientes para este aluguel!")
            if modo_aluguel.lower() != 'hora' and modo_aluguel.lower() != 'dia' and modo_aluguel.lower() != 'semana':
                print('Só é possível alugar por hora, dia ou semana!')
            if (modo_aluguel == 'hora' and duracao >= 24) or (modo_aluguel == 'dia' and duracao >= 7) or (duracao <= 0) or (modo_aluguel == 'semana' and duracao >= 52):
                if self.modo_aluguel == 'hora':
                    print('Não é possível alugar mais que 24 horas seguidas. Escolha o aluguel por dia.')
                elif self.modo_aluguel == 'dia':
                    print('Não é possível alugar mais que 7 dias seguidos. Escolha o aluguel por semana.')
                elif self.modo_aluguel == 'semana':
                    print('Não é possível alugar mais que 52 semanas seguidas.')
                elif self.duracao <= 0:
                    print('Nao é possível alugar com um duração de zero ou um número negativo!')
            else:
                self.numero_bicicletas_alugadas = numero_bicicletas_alugadas
                self.duracao = duracao
                self.alugueis_ativos.append({'cpf':cpf, 'n_alugadas':{}})
        
        #     # tratar outros possíveis erros nos atributos do construtor
        #     # (modo de aluguel só pode ser "hora", "dia", "semana")

        # depois ver com fazer o cliente devolver as bicicletas para poder fazer novo aluguel.
        # (talvez na hora de calcular valor?)                    

        # coloquei um previsão para gravar os modelos e numeros de bicicletas alugadas por cada cliente no
        # no dicionario na chave 'n_alugadas' em alugueis.ativos. Não tive tempo de fazer gravar essa informação.
        # Com essa informação de cada aluguel na chave 'n_alugadas' seria possível não apenas saber modelo e 
        # quantidade de bicicletas alugadas por cada cliente, mas gravar mais de um aluguel por cliente.
                print("Número de bicicletas atualmente disponíveis:", self.total_de_bicicletas)
                print("Bicicletas alugadas pelo cliente:", self.numero_bicicletas_alugadas)
        # comecar fazendo com duracao previa, mas pensar no futuro em usar o datetime pra registrar o momento do aluguel 
        # e na loja registrar o momento de devolucao pra calcular o valor do aluguel
                bikes_alugadas = self.numero_bicicletas_alugadas
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
        # valor por tipo de aluguel (R$5/hora, R$25/dia, R$100/semana)
        h = 5
        d = 25
        s = 100
        valor = cliente.duracao * self.cliente.numero_bicicletas_alugadas
        if len(self.alugueis_ativos) == 0:
            print('Não há alugueis ativos! Não é possível calcular o valor.')
        # elif self.cliente.numero_bicicletas_alugadas == 0:
        #     print('Não há alugueis ativos! Não é possível calcular o valor.')
        elif (cliente.numero_bicicletas_alugadas) >= 3:
            desconto = 30 / 100
            if cliente.modo_aluguel == 'hora':
                preco_final = (valor * h)
            elif cliente.modo_aluguel == 'dia':
                preco_final = (valor * d)
            elif cliente.modo_aluguel == 'semana':
                preco_final = (valor * s)
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

    # @staticmethod
    # def lista_de_clientes():
    #     print(Loja.clientes)

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

# cliente1 = Cliente('John', 50, 'dia', 3)
cliente1 = Cliente('John', '00000000001')
print(Loja.clientes)
# Loja.lista_de_clientes
# cliente2 = Cliente('João', 3, 'hora', 5)
cliente2 = Cliente('João', '00000000002')
# cliente3 = Cliente('Danielle', 2, 'semana', 2)
cliente3 = Cliente('Danielle', '00000000003')

# cliente4 = Cliente('Michael', 1, 'hora', 50)
# cliente5 = Cliente('Dwight', 1, 'dia', 10)
# cliente6 = Cliente('Pike', 1, 'semana', 10)

# print(cliente1.nome, cliente1.numero_bicicletas_alugadas, cliente1.modo_aluguel, cliente1.duracao)

# loja1(cliente2) # funcionava e parou, pq?

# loja1.recebe_aluguel(cliente1)

# loja1.recebe_aluguel(cliente2)

# print(loja1.total_de_bicicletas)
# print(loja1.estoque)
# print(cliente2.nome, cliente2.numero_bicicletas_alugadas, cliente2.modo_aluguel, cliente2.duracao)

# loja1.recebe_aluguel(cliente1)

cliente1.ver_estoque(loja1)
cliente3.ver_estoque(loja2)

#loja2.recebe_aluguel(cliente4)
# print(loja2.estoque)


cliente1.alugar_bicicleta(8, 'dia', 3, loja1)
cliente2.alugar_bicicleta(5, 'semana', 8, loja1)

loja1.calcular_valor(cliente1)
print(loja1.alugueis_ativos)