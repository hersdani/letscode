# Exercício 03

# Dois dicionários que tem como chave o mês: Um dos dicionários vai ter valor a quantidade de horas trabalhadas no mês; O outro, terá
# a quantidade de slário-hora

#Eles devem ser criados sentro da classe

class Funcionario:
    def __init__(self,nome,email):
        self.nome =  nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if (mes not in self.horas):
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
        if (mes not in self.salario_hora):
            self.salario_hora[mes] = valor 


    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print('Mês Inexistente!!')
        else:
            return self.horas[mes] * self.salario_hora[mes]

    def __repr__(self):

        return f'Funcionário: {self.nome}, \nEmail: {self.email}, \nhoras/mês: {self.horas}, \nsalário-hora: {self.salario_hora}'


funcionario = Funcionario('Matheus', 'matheus@letscode.com.br')

funcionario.cadastro_hora('Jan', 300)
funcionario.cadastro_hora('Fev', 200)
funcionario.cadastro_salario_hora('Jan', 30)
funcionario.cadastro_salario_hora('Fev', 30)
print(funcionario)
print(funcionario.calcula_salario('Jan'))
print(funcionario.calcula_salario('Fev'))