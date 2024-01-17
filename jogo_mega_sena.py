from random import sample


# gera sequencia aleatoria, sem repetição, de números entre 1 e 60
def gerar_jogo(dezenas_quantidade):
    print(sorted(list(sample(range(1, 61), dezenas_quantidade))))


# gera uma lista, contendo as varias sequencias númericas, ilimitado a quantidade de jogos desejada
def gerar_lista_jogos(jogos_quantidade, dezenas_quantidade):
    lista_jogos = list()
    while len(lista_jogos) <= jogos_quantidade:
        lista_jogos.append(
            gerar_jogo(dezenas_quantidade)
        )
    print(lista_jogos)


gerar_lista_jogos(5, 6)
gerar_jogo(6)
