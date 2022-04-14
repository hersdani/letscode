1. Classe Bola: Crie uma classe que modele uma bola:
    - Atributos: Cor, circunferência, material
    - Métodos: trocaCor e mostraCor

2. Classe Quadrado: Crie uma classe que modele um quadrado:
    - Atributos: Tamanho do lado
    - Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

3. Classe Retangulo: Crie uma classe que modele um retangulo:

    - Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    - Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    - Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidas de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local. O programa também deve pedir as medidas de cada piso e rodapé

4. Classe Pessoa: Crie uma classe que modele uma pessoa:
    - Atributos: nome, idade, peso e altura
    - Métodos: Fazer aniversario, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa faz aniversário, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

5. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente
    - Atributos: número da conta, nome do correntista e saldo
    - Métodos: alterar_nome, deposito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
6. Classe carro: Implemente uma classe chamada Carro com as seguintes          propriedades:
    - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.

    - O consumo é especificado no construtor e o nível de combustível inicial é 0.

    - Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
    - Forneça um método obter_gasolina(), que retorna o nível atual de combustível.
    - Forneça um método adicionar_gasolina(), para abastecer o tanque. Exemplo de uso:
    ```
    meu_carro = Carro(15);           # 15 quilômetros por litro de combustível. 
    meu_carro.adicionar_gasolina(20); # abastece com 20 litros de combustível. 
    meu_carro.andar(100);            # anda 100 quilômetros.
    meu_carro.obter_gasolina()        # Imprime o combustível que resta no tanque.
    ```

7. Classe Conta de Investimento: Faça uma classe ContaInvestimento que seja semelhante a classe de conta corrente, com a diferença de que se adicione um atributo taxa_juros.

    Forneça um construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicione_juros (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicione_juros() cinco vezes e imprime o saldo resultante.

