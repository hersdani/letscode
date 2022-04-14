# exercício 01
nomes = ["André", "João", "Maria"]
arquivo = open('nomes.txt', 'w', encoding='UTF-8') # Criar o arquivo
for x in range(len(nomes)):
    arquivo.write(nomes[x]+'\n')
arquivo.close()

# exercício 02
import csv
notas_alunos = [['jose', 10, 8, 9.5, 8.8, 10],
                ['pedro', 9.8, 9.2, 9.0, 8.8, 9.1],
                ['suzana', 8, 7.1, 7.5, 8.2, 7.9],
                ['gisela', 10, 9.6, 8.9, 9.4, 9.7],
                ['joao', 7.5, 7.9, 8.0, 9.1, 7.3]]

arquivo = open('notas_alunos.csv', 'w')

escritor = csv.writer(arquivo, lineterminator='\n')

escritor.writerows(notas_alunos) # Escreve a tabela

arquivo.close()

# exercício 03
import csv

arquivo = open('notas_alunos.csv', 'a')

escritor = csv.writer(arquivo, lineterminator='\n')

escritor.writerows([['mariana',8.9,10,9.7,9.0,9.2],['luciana',9.5,8.7,10,9.4,9.6]]) # Escreve a tabela

arquivo.close()

# exercício 04
import csv
arquivo = open('notas_alunos.csv', 'r')

leitor = csv.reader(arquivo, delimiter=',', lineterminator='\n')

tabela = []

for linha in leitor:
    tabela.append(linha)

notas = []

for linha in tabela:
    nota = 0
    for x in range(len(linha)-1):
        nota += float(linha[x+1])
    media = nota/5
    notas.append(linha[0]+' - '+str(media))

print(notas)
