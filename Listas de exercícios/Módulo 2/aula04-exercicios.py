'''
1. Classe Bola: Crie uma classe que modele uma bola:
    - Atributos: Cor, circunferência, material
    - Métodos: trocaCor e mostraCor
    '''

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        #nova_cor = input('Digite a nova cor:')
        self.cor = nova_cor
    
    def mostraCor(self):
        return self.cor

bola1 = Bola('vermelha', 4, 'alumínio')

bola1.trocaCor('azul')

print(bola1.mostraCor)

bola1.mostraCor()


'''
2. Classe Quadrado: Crie uma classe que modele um quadrado:
    - Atributos: Tamanho do lado
    - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
'''

class Quadrado:

    def __init__(self, tam_lado):
        self.tam_lado = tam_lado

    def muda_lado(self, novo_tam_lado):
        self.tam_lado = novo_tam_lado

    def retorna_lado(self):
        return self.tam_lado

    def area(self):
        area = self.tam_lado ** 2
        return area

quadrado1 = Quadrado(8)
quadrado1.retorna_lado()
quadrado1.area()


'''
3. Classe Retangulo: Crie uma classe que modele um retangulo:
    - Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    - Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    - Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. 
    Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. 
    O programa também deve pedir as medidas de cada piso e rodapé
'''

class Retangulo:

    def __init__(self, lado_A, lado_B):
        self.lado_A = lado_A
        self.lado_B = lado_B
    
    def muda_lados (self, novo_A, novo_B):
        self.lado_A = novo_A
        self.lado_B = novo_B
    
    def return_lado(self):
        return self.lado_A, self.lado_B
    
    def area(self):
        area = self.lado_A * self.lado_B
        return area
    
    def perimetro(self):
        perimetro = 2 * self.lado_A + 2 * self.lado_B
        return perimetro
    
retangulo1 = Retangulo(2, 4)
retangulo1.return_lado()

retangulo1.muda_lados(3, 3)
retangulo1.return_lado()

retangulo1.area()
retangulo1.perimetro()

# medida1 = input('Informe a ')

'''
daqui pra baixo foi o Matheus que fez
'''

piso = Retangulo(5, 10)
azulejo = Retangulo(0.1, 0.1)

area_piso = piso.area()
area_azulezo = azulejo.area()

n_azulejos = area_piso / area_azulezo

if n_azulejos = 

print(f'A quantide de azulejos para preencher o piso é de {n_azulejos}')

#ver o restante no arquivo do professor

