'''
Questão #1
Crie uma classe Bola cujos atributos são cor e raio. Crie um método que imprime a cor da bola. Crie um método para calcular a área dessa bola. Crie um método para calcular o volume da bola. Crie um objeto dessa classe e calcule a área e o volume, imprimindo ambos em seguida.
Obs.:
Área da esfera = 4*3.14*r*r;
Volume da esfera = 4*3.14*r*r*r/3
'''

import mailbox


class Bola:
    def __init__(self,cor, raio):
        self.cor = cor
        self.raio = raio
    def cor(self):
        print(self.cor)
    def area(self):
        ar = 4*3.14*(self.raio**2)
        return ar
    def volume(self):
        vol = (4*3.14*(self.raio**3))/3
        return vol


bola1 = Bola('Azul', 10)

print(bola1.area())
print(bola1.volume())


print(f'A area superficial da bola 1 é {bola1.area():.2f}')
print(f'O volume da bola 1 é {bola1.volume():.2f}')


'''
Questão #2
Crie uma classe Retângulo cujos atributos são lado_a e lado_b. Crie um método para calcular a área desse retângulo. Crie um objeto dessa classe e calcule a área e a imprima em seguida.
'''
class Retangulo:
    def __init__(self,lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b
    def area(self):
        area = self.lado_a * self.lado_b
        return area

retangulo1 = Retangulo(7.5, 12.5)

print(retangulo1.area())
print(f'A area superficial da bola 1 é {retangulo1.area():.2f}')

'''
Questão #3
Crie uma classe Funcionario cujos atributos são nome e e-mail. Guarde as horas trabalhadas em um dicionário cujas chaves são o mês em questão e, em outro dicionário, guarde o salário por hora relativo ao mês em questão. Crie um método que retorna o salário mensal do funcionário.
'''

class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if mes not in self.horas:
            self.horas[mes] = horas
        
    def cadastro_salario_hora(self, mes, valor):
        if mes not in self.salario_hora:
            self.salario_hora[mes] = valor

    def salario(self, mes):
        if mes not in self.horas:
            print('Não há dados de horas trabalhadas no mês informado!')
        elif mes not in self.salario_hora:
            print('Não há dados de salário por hora trabalhada no mês informado!')
        else:
            return self.horas[mes] * self.salario_hora[mes]

funcionario = Funcionario('Matheus', 'matheus@letscode.com.br')

funcionario.cadastro_hora('Jan', 300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 30)
funcionario.cadastro_salario_hora('Fev', 30)
print(funcionario.salario('Jan'))


    
'''
Questão #4
Crie uma classe Televisor cujos atributos são:
a. fabricante;
b. modelo;
c. canal atual;
d. lista de canais; e
e. volume.
Faça métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista). No atributo lista de canais, devem estar armazenados todos os canais já sintonizados dessa TV.
Obs.: O volume não pode ser menor que zero e maior que cem; só se pode trocar para um canal que já esteja na lista de canais.
'''

class Televisor:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = None
        self.lista_canais = []
        self.volume = 20

    def troca_canal(self, canal):        
        if canal in self.lista_canais:
            self.canal_atual = canal
    
    def novo_canal(self, canal):
        if canal not in self.lista_canais:
            self.lista_canais.append(canal)
    
    def aumenta_volume(self, valor):
        if self.volume + valor <= 100:
            self.volume += valor
        else:
            self.volume = 100

    def diminui_volume(self, valor):
        if self.volume - valor >= 0:
            self.volume -= valor
        else:
            self.volume = 0

    def __repr__(self):
        return f'O Televisor é do fabricante {self.fabricante} modelo {self.modelo}'

tv1 = Televisor('CCE','XPTO-123')

print(tv1)

tv2 = Televisor("Toshiba","mk2")
tv2.aumenta_volume(30)
tv2.diminui_volume(100)

tv2.novo_canal('Globo')
tv2.novo_canal('SBT')
tv2.troca_canal('Globo')

print(tv2.lista_canais)
print(tv2.canal_atual)

print(tv2.volume)

len(tv2)

'''
Questão #5
Crie uma classe ControleRemoto cujo atributo é televisão (isso é, recebe um objeto da classe do exercício 4). Crie métodos para aumentar/diminuir volume, trocar o canal e sintonizar um novo canal, que adiciona um novo canal à lista de canais (somente se esse canal não estiver nessa lista).
'''

class ControleRemoto:
    def __init__(self, tv):
        self.tv = tv
    def aumentaVolume(self):
        self.tv.aumenta_volume(10)
    def diminuiVolume(self):
        self.tv.diminui_volume(10)
    def troca_canal(self, canal):
        self.tv.troca_canal(canal)
    def novo_canal(self, canal):
        self.tv.novo_canal(canal)


tv = Televisor('SONY','SONY-123')

controle = ControleRemoto(tv)

controle.novo_canal('SBT')
controle.troca_canal('SBT')

print(tv.canal_atual)

controle.aumentaVolume()
print(tv.volume)

controle.diminuiVolume()

print(tv.volume)



'''
Questão #6
O módulo time possui a função time.sleep(x), que faz seu programa “dormir” por x segundos. Utilizando essa função, crie uma classe Cronômetro e faça um programa que cronometre o tempo.
'''

class Cronometro:

    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def incremento(self):
        self.segundos += 1
        if self.segundos >= 60:
            self.segundos = 0
            self.minutos += 1
        if self.minutos >= 60:
            self.minutos = 0
            self.horas += 1

    def __repr__(self):
        return f'{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}'

    def iniciar(self):
        from time import sleep
        from os import system
        while True:
            system('cls')
            print(self)
            self.incremento()
            sleep(1)

c1 = Cronometro()
c1.iniciar()


'''
Questão #7
Crie uma modelagem de classes para uma agenda capaz de armazenar contatos. Através dessa agenda é possível incluir, remover, buscar e listar contatos já cadastrados.
'''



'''
Questão #8
Crie uma classe Cliente cujos atributos são nome, idade e e-mail. Construa um método que imprima as informações tal como abaixo:

Nome: Fulano de Tal
Idade: 40
E-mail: fulano@mail.com
'''



'''
Questão #9
Com base no exercício anterior, crie um sistema de cadastro e a classe Cliente. Seu programa deve perguntar se o usuário quer cadastrar um novo cliente, alterar um cadastro ou sair.
Dica: Você pode fazer esse exercício criando uma classe Sistema, que irá controlar o sistema de cadastros. Essa classe deve ter o atributo cadastro e os métodos para imprimir os cadastrados, cadastrar um novo cliente, alterar um cadastro ou sair.
'''


'''
Questão #10
Crie uma classe ContaCorrente com os atributos cliente (que deve ser um objeto da classe Cliente) e saldo. Crie métodos para depósito, saque e transferência. Os métodos de saque e transferência devem verificar se é possível realizar a transação.
'''


'''
Questão #11
Crie uma classe Fração cujos atributos são numerador (número de cima) e denominador (número de baixo).
Implemente os métodos de adição, subtração, multiplicação, divisão que retornam objetos do tipo Fração.
Implemente também o método _ repr _.
Implemente métodos para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).
'''



'''
Questão #12
Crie uma classe Data cujos atributos são dia, mês e ano. Implemente métodos _ repr _ e para comparação: igualdade (==) e desigualdades (!=, <=, >=, < e >).
'''


'''
Questão #13
Nos exercícios 1, 2, 3, 4 e 6, implemente o método _ repr _ para exibir as informações desejadas de cada uma das classes.
'''



'''
Questão #14
Crie uma classe Quadrado, filha da classe Retângulo do exercício 2.
'''


'''
Questão #15
Faça uma classe ContaVip que difere da ContaCorrente por ter cheque especial (novo atributo) e é filha da classe ContaCorrente. Você precisa implementar os métodos para saque, transferência ou depósito?
'''


