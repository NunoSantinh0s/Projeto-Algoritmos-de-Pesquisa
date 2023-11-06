import random

def criar_ficheiro_desordenado(nome_ficheiro, quantidade, valor_max):
    with open(nome_ficheiro, 'w') as ficheiro:
        for _ in range(quantidade):
            numero = random.randint(0, valor_max)
            ficheiro.write(str(numero) + '\n')

def criar_ficheiro_ordenado(nome_ficheiro, quantidade, valor_max):
    with open(nome_ficheiro, 'w') as ficheiro:
        numeros = [random.randint(0, valor_max) for _ in range(quantidade)]
        numeros.sort()
        for numero in numeros:
            ficheiro.write(str(numeros) + '\n')

quantidades = [100, 1000, 10000, 100000]
valor_max = 1000000

for quantidade in quantidades:
    nome_ficheiro_desordenado = f'desordenado_{quantidade}.txt'
    nome_ficheiro_ordenado = f'ordenado_{quantidade}.txt'

    criar_ficheiro_desordenado(nome_ficheiro_desordenado, quantidade, valor_max)
    criar_ficheiro_ordenado(nome_ficheiro_ordenado, quantidade, valor_max)

