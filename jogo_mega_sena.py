
# Gerador de Jogos da Mega Sena

# Importando a biblioteca random
from random import sample


# Gerando sequencia aleatória, sem repetição, de números entre 1 e 60
def gerar_jogo(dezenas):
    return sorted(list(sample(range(1, 61), dezenas)))


# Gerando uma lista, contendo as varias sequencias númericas, ilimitado a quantidade de jogos desejada
def gerar_lista_jogos(jogos, dezenas):
    lista_jogos = list()

    while len(lista_jogos) <= jogos:
        lista_jogos.append(
            gerar_jogo(dezenas)
        )
    return lista_jogos


# Resultado
print("[ GERADOR DE JOGOS DA MEGA SENA ]")
quantidade_de_jogos = int(input("\n-Digite a quantidade de jogos que deseja fazer: "))

lista_final = gerar_lista_jogos((quantidade_de_jogos - 1), 6)

for n in range(quantidade_de_jogos):
    print(lista_final[n])
