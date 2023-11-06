def pesquisa_sequencial(lista, item):
    encontrado = False
    for elemento in lista:
        if elemento == item:
            encontrado = True
            break
    return encontrado
        

def pesquisa_sequencial_recursiva(lista, n):
    if lista[0] == n:
        return True
    if len(lista) == 1:
        return False
    return pesquisa_sequencial_recursiva(lista[1:], n)


def pesquisa_binaria(lista, item):
    with open(lista, 'r') as ficheiro:
        linhas = ficheiro.readlines()
        inteiros = [int(numero) for linha in linhas for numero in linha.strip().replace('[', '').replace(']', '').split(',')]


    
    primeiro = 0
    ultimo = len(inteiros) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if inteiros[meio] == item:
            return True
        else:
            if item < inteiros[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False



def pesquisa_binaria_recursiva(lista, item, inicio=0, fim=None):
    with open(lista, 'r') as ficheiro:
        linhas = ficheiro.readlines()
        inteiros = [int(numero) for linha in linhas for numero in linha.strip().replace('[', '').replace(']', '').split(',')]
    
    if fim is None:
        fim = len(lista)

    if inicio >= fim:
        return False

    meio = (inicio + fim) // 2
    if inteiros[meio] == item:
        return True
    elif int(item) < int(inteiros[meio]):
        return pesquisa_binaria_recursiva(lista, item, inicio, meio)
    else:
        return pesquisa_binaria_recursiva(lista, item, meio + 1, fim)
    




