
# fazer tratamento de excecoes com raide e/ou try/except
class Cliente:
    def __init__(self, nome, numero_bicicletas_alugadas, modo_aluguel, duracao):
        self.nome = nome
        # pensar depois numa forma de fazer q no futuro trabalhe com cadastro de clientes separado, 
        # talvez numa outra classe ou arquivo com tabela ou dicionario.
        if numero_bicicletas_alugadas <= 0:
            print('Não é possível alugar zero ou um número negativo de bicicletas')
        else:    
            # tratar outros possíveis erros nos atributos do construtor
            # (modo de aluguel só pode ser "hora", "dia", "semana")
            self.numero_bicicletas_alugadas = numero_bicicletas_alugadas
        if modo_aluguel.lower() != 'hora' and modo_aluguel.lower() != 'dia' and modo_aluguel.lower() != 'semana':
            print('Só é possível alugar por hora, dia ou semana!')
        else:
            self.modo_aluguel = modo_aluguel
        #(duração > 0 - colocar um limite? hora < 24h, dia < 7, semana xxx?)
        if (modo_aluguel == 'hora' and duracao >= 24) or (modo_aluguel == 'dia' and duracao >= 7):
            if modo_aluguel == 'hora':
                print('Não é possível alugar mais que 24 horas seguidas. Escolha o aluguel por dia.')
            if modo_aluguel == 'dia':
                print('Não é possível alugar mais que 7 dias seguidos. Escolha o aluguel por semana.')
        else:
            self.duracao = duracao 
        # comecar fazendo com duracao previa, mas pensar no futuro em usar o datetime pra registrar o momento do aluguel 
        # e na loja registrar o momento de devolucao pra calcular o valor do aluguel
    
    # metodos:

    # ver bicicletas disponíveis na loja (fazer depois de fazer a classe Loja)
    def consultar_estoque(self, loja):
        print('-----------------------------------------------------')
        print(f"{'  '}{'Modelo':<15s}|{'     '}{'Cor':<15s}|{'    '}{'Estoque':>10s}")
        print('-----------------------------------------------------')
        for elemento in loja.estoque:
            print(f"{'  '}{elemento['id']:<15s}|{'     '}{elemento['cor']:<15s}|{'    '}{elemento['estoque']:>10d}")

        print('-----------------------------------------------------')
        print('A loja tem', loja.total_de_bicicletas, 'bicicletas disponíveis para locação.')
        print('-----------------------------------------------------')
        #print(loja.estoque)

    # receber o modo de aluguel e calcular o valor no metodo da loja calcula_valor
    # alugar bicicletas por R$5 / hora
    # alugar bicicletas por R$25 / dia
    # alugar bicicletas por R$100 / semana 

    # seria possivel fazer um metodo unico informando o modo de aluguel (hora, dia, semana) e o valor por intervalo (o valor pode ficar na loja na hora de calcular o valor)?

    # def alugar_bicicleta(self):
    #     if self.numero_bicicletas_alugadas >= 3:
    #         self.valor = =....
    #     if self.modo_aluguel == 'hora':

    #     if self.modo_aluguel == 'dia':

    #     pass

    # condicional nos outros metodos ou fazer um outro metodo? alugar bicicletas plano familia - 3 ou mais emprestimos 
    # de qualquer tipo com 30% de desconto no valor total



class Loja:
    estoque_padrao = [{'id': 'Bike1', 'cor': 'vermelha', 'estoque': 8 },
             {'id': 'Bike2', 'cor': 'azul', 'estoque': 7},
             {'id': 'Bike3', 'cor': 'preta', 'estoque': 9},
             {'id': 'Bike4', 'cor': 'amarela', 'estoque': 6},
             {'id': 'Bike4', 'cor': 'preta', 'estoque': 10 }]
    def __init__(self, estoque=estoque_padrao):
        # fazendo com atributo estoque padrão fora do contrutor é possivel colocar um estoque padrão para cada loja, mas alterar caso queira
        # depois pensar na possibilidade de fazer uma classe de bicicletas para entrada de estoque e saída de estoque, com a Loja chamando esta classe
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
            ## (self.total_de_bicicletas) -= (cliente.numero_bicicletas_alugadas)
            # como dar baixa das bicicletas alugadas na lista do estoque? 
            # Seria melhor dar baixa em self.estoque e e depois contar o total_de_bicicletas a partir dele.
            # talvez com um:
            # for elemento in self.estoque:
            #     if elemento['estoque'] == 0:
            #         continue
            #     elif (elemento['estoque'] > 0):
            #         if (elemento['estoque'] < cliente.numero_bicicletas_alugadas):
            #             elemento['estoque'] =- elemento['estoque']
            #             cliente.numero_bicicletas_alugadas = cliente.numero_bicicletas_alugadas - elemento['estoque']
            #             continue
            #         else:
            #             elemento['estoque'] =- cliente.numero_bicicletas_alugadas
                       
            for i in self.estoque:
                if bikes_alugadas == 0:
                    break
                if i['estoque'] == 0:
                    continue

                ## teste1 ##
                # elif (i['estoque'] > 0):
                #     print('for1. estoque do elemento', i, 'antes do 2o. if = ', i['estoque'])
                #     print('for1. bicicletas alugadas antes do 2o. if', bikes_alugadas)
                #     for j in self.estoque:
                #         if (j['estoque'] < bikes_alugadas):
                #             j['estoque'] -= j['estoque']
                #             bikes_alugadas = bikes_alugadas - j['estoque']
                #             print('for2. estoque do elemento', j, 'depois do 2o. if = ', j['estoque'])
                #             print('for2. bicicletas alugadas', j, 'depois do 2o. if', bikes_alugadas)
                #             continue
                #         else:
                #             i['estoque'] -= bikes_alugadas
                #             print('for2.estoque do elemento', j, 'depois do else = ', j['estoque'])
                #             print('for2.bicicletas alugadas', j, 'depois do else', bikes_alugadas)
                
                ## teste3 ##
                elif (i['estoque'] > 0):
                    if (i['estoque'] < bikes_alugadas):
                        # print(i['estoque'], 'estoque antes de alugar')
                        # print(bikes_alugadas, 'bikes alugadas antes de alugar')
                        bikes_alugadas = bikes_alugadas - i['estoque']
                        i['estoque'] -= i['estoque']
                        # print(i['estoque'], 'estoque depois de alugar')
                        # print(bikes_alugadas, 'bikes alugadas depois de alugar')
                        # continue
                    elif i['estoque'] >= bikes_alugadas:
                        # print(bikes_alugadas, 'antes de subtrair')
                        i['estoque'] -= bikes_alugadas
                        bikes_alugadas = 0
                        # print(bikes_alugadas, 'depois de subtrair')

            #será que tem como usar algo do construtor pra calcular o estoque? ou colocar esse for separado em outro metodo?
            self.total_de_bicicletas = 0
            for k in self.estoque:
                self.total_de_bicicletas += k['estoque']     
            print("Número de bicicletas disponíveis após o aluguel:", self.total_de_bicicletas)
            # calcula_estoque_total()
            # print("Aluguel possível! Número de bicicletas disponíveis após este aluguel:", self.total_de_bicicletas)

        # com datetime receber o momento da devolucao e fazer a conta com o inicio do aluguel
        # pass

    # calcular a conta qdo o cliente devolver a bicicleta
    def calcula_valor():
        # if (cliente.numero_bicicletas_alugadas) > 3:

        pass
    
    # mostrar o estoque de bicicletas
    def mostra_estoque(self):
        #for elemento in self:
        pass



loja1 = Loja()
print(loja1.total_de_bicicletas)
print(loja1.estoque)

estoque2 = [{'id': 'Bike1', 'cor': 'vermelha', 'estoque': 8 },
             {'id': 'Bike2', 'cor': 'azul', 'estoque': 7},
             {'id': 'Bike4', 'cor': 'preta', 'estoque': 9},
             {'id': 'Bike5', 'cor': 'amarela', 'estoque': 6},
             {'id': 'Bike9', 'cor': 'preta', 'estoque': 10 },
             {'id': 'Bike9', 'cor': 'azul', 'estoque': 10 }]
loja2 = Loja(estoque2)
print(loja2.total_de_bicicletas)
print(loja2.estoque)

cliente1 = Cliente('John', 50, 'dia', 3)

cliente2 = Cliente('João', 3, 'hora', 5)

cliente3 = Cliente('Danielle', 10, 'semana', 2)

# print(cliente1.nome, cliente1.numero_bicicletas_alugadas, cliente1.modo_aluguel, cliente1.duracao)



# loja1(cliente2) # funcionava e parou, pq?

loja1.recebe_aluguel(cliente1)

loja1.recebe_aluguel(cliente2)

print(loja1.total_de_bicicletas)
print(loja1.estoque)
print(cliente2.nome, cliente2.numero_bicicletas_alugadas, cliente2.modo_aluguel, cliente2.duracao)


loja1.recebe_aluguel(cliente3)

cliente1.consultar_estoque(loja1)
cliente3.consultar_estoque(loja2)