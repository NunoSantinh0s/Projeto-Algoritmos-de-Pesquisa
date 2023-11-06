import time
import statistics
import matplotlib.pyplot as plt

def duracao(funcao, nome_ficheiro, item, n_vezes):
    tempos_execucao = []

    for i in range(n_vezes):
        inicio = time.time()
        resultado = funcao(nome_ficheiro, item)
        fim = time.time()
        tempos_execucao.append(fim - inicio)
    
    tempo_medio = statistics.mean(tempos_execucao)
    desvio_padrao = statistics.stdev(tempos_execucao)

    return tempos_execucao, tempo_medio, desvio_padrao

def complexidade(funcao, nome_ficheiro, lista_items, n_vezes):
    dic_stats = {}
    dic_tempos = {}

    for item in lista_items:
        tempos_execucao, tempo_medio, desvio_padrao = duracao(funcao, nome_ficheiro, item, n_vezes)
        dic_stats[item] = (tempo_medio, desvio_padrao)
        dic_tempos[item] = tempos_execucao

    return dic_stats, dic_tempos

def boxplot(lista_tempos_execucao):
    plt.boxplot(lista_tempos_execucao)
    plt.show()

def complexidade_boxplot(dic_tempos):
    fig, ax = plt.subplots()
    ax.boxplot(dic_tempos.values())
    ax.set_xticklabels(dic_tempos.keys())
    ax.set_xticklabels(dic_tempos.keys(), rotation=90)
    ax.set_xlabel('Valor do input')
    ax.set_ylabel('Tempo de execução da função')

    plt.show()
