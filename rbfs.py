def objetivo_alcancado(atual, objetivo):
    return atual == objetivo


def funcao_sucessora(atual, labirinto):
    sucessores = []
    movimentos = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for movimento in movimentos:
        nova_posicao = (atual[0] + movimento[0], atual[1] + movimento[1])
        if 0 <= nova_posicao[0] < len(labirinto) and 0 <= nova_posicao[1] < len(
                labirinto[0]) and labirinto[nova_posicao[0]][nova_posicao[1]] != "#":
            sucessores.append(nova_posicao)
    return sucessores


def funcao_heuristica(atual, objetivo):
    return ((atual[0] - objetivo[0]) ** 2 + (atual[1] - objetivo[1]) ** 2) ** 0.5


def busca_recursiva_melhor_escolha(atual, objetivo, labirinto, caminho):
    caminho.append(atual)
    if objetivo_alcancado(atual, objetivo):
        return caminho
    sucessores = funcao_sucessora(atual, labirinto)
    custo_estimado = {}
    for sucessor in sucessores:
        custo_estimado[sucessor] = funcao_heuristica(sucessor, objetivo)
    proximo_estado = min(custo_estimado, key=custo_estimado.get)
    return busca_recursiva_melhor_escolha(proximo_estado, objetivo, labirinto, caminho)


labirinto = [
    ['#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#']
]
inicio = (1, 1)
objetivo = (3, 3)
caminho = []
resultado = busca_recursiva_melhor_escolha(inicio, objetivo, labirinto, caminho)
print(resultado)
