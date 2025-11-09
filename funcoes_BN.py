import random

# criacao das 4 matrizes  necessarias

matrizJogador = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matrizPc = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matrizAuxiliar = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

matrizAuxiliar2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


# funcao que mostra a tela inicial
def inicio():
    print('Bem vindo ao seu jogo de batalha naval!')
    print('O objetivo do jogo é afundar a tropa de navios do inimigo')
    print('\n')
    print('Deseja ver as regras de maneira detalhada?')
    opcao = input('S para sim\nN para não\nSua opção: ').strip().upper()
    while opcao != 'S' and opcao != 'N':  # laço para garantir que seja digitado corretamente
        opcao = input('S para sim\nN para não\nSua opção: ').strip().upper()
    print('\n')
    if opcao == 'S':  # regras do jogo
        print("\n--- REGRAS DA BATALHA NAVAL ---")
        print("1. Tabuleiro: É definido um tabuleiro (matriz) de 5x10 ou 10x10.")
        print("   (Os tabuleiros não são visíveis para os jogadores).")
        print("\n2. Preparação: Antes de iniciar, os jogadores posicionam sua frota")
        print("   em seu tabuleiro, sem revelar ao adversário.")
        print("\n3. Turnos: As jogadas são feitas de forma alternada.")
        print("\n4. O Tiro: No seu turno, o jogador 'atira' em uma posição do")
        print("   tabuleiro adversário, indicando as coordenadas (linha e coluna).")
        print("\n5. Resultado: O jogo informa se o tiro acertou algo ou não.")
        print("   (Se acertar, a embarcação foi afundada).")
        print("\n6. Vitória: Ganha o jogo quem afundar primeiro a frota do adversário.")
        print("---------------------------------\n")


# funcao que mostra o tabuleiro para o jogador se guiar
def mostrarTabuleiro():
    print('Para começar, vamos definir o posicionamento de suas embarcações')
    print('Abaixo segue o tabuleiro:')

    for i in range(len(matrizAuxiliar)):  # laço para mostrar o tabuleiro vazio
        print(matrizAuxiliar[i])


# funcao que cria as embarcacoes do jogador
def definirEmbarcacoes():
    embarcacoes = 0  # variavel para mostrar o número de cada embarcação
    while embarcacoes < 5:
        linha = int(input(f'Digite o número da linha que deseja posicionar a embarcação número {embarcacoes + 1} (1 a 5): ')) - 1  # -1 usado para garantir que o usuario possa 1 digitar o que ele ve, ex: 1 e nao 0
        col = int(input(f'Digite o número da coluna que deseja posicionar a embarcação número {embarcacoes + 1} (1 a 10): ')) - 1
        if matrizJogador[linha][col] != 'X':  # verificação para o usuario não repetir a posição
            matrizJogador[linha][col] = 'X'
            embarcacoes += 1
    print('\n')
    for j in range(5):  # laço para mostrar o tabuleiro preenchido do jogador ao final
        print(matrizJogador[j])


# funcao que cria as embarcacoes do pc
def definirEmbarcacoesPc():
    embarcacoes = 0
    while embarcacoes < 5:  # looping de sorteio das posições do pc
        linha = random.randint(0, 4)
        col = random.randint(0, 9)
        if matrizPc[linha][col] != 'X':  # verificação para garantir que o pc não repita a posição de sorteio
            matrizPc[linha][col] = 'X'
            embarcacoes += 1


# funcao que mostra os tabuleiros de ambos os jogadores com os 2 parametros de 'vida' dos players
def mostrarFrota(embarcacoesPlayer, embarcacoesPc):
    print('-----------sua frota----------')
    print(f'(----embarcações player: {embarcacoesPlayer}-----')
    for i in range(5):
        print(f'{matrizAuxiliar[i]}')  # bloco que mostra as embarcações do player
    print('\n')
    print('---------frota do pc----------')
    print(f'-------embarcações pc: {embarcacoesPc}------')
    for i in range(5):
        print(f'{matrizAuxiliar2[i]}')  # bloco que mostra as embarcações do pc


# funcao com toda a lógica de jogabilidade
def jogada():
    embarcacoesPlayer = 5  # embarcações restantes do player
    embarcacoesPc = 5  # embarcações restantes do pc

    # looping que roda até que um dos jogadores perca todas as embarcações
    while embarcacoesPlayer != 0 and embarcacoesPc != 0:
        # chamada da função de mostrar os tabuleiros com as embarcações restantes como parametro
        mostrarFrota(embarcacoesPlayer, embarcacoesPc)
        # verificação para garantir que o jogador só jogue se tiver embarcações
        if embarcacoesPlayer > 0:
            jogadaLinhaPlayer = int(input('Digite o número da linha que deseja atacar o computador (1 a 5): ')) - 1
            while jogadaLinhaPlayer < 0 or jogadaLinhaPlayer >= 5:  # laço para o jogador só digitar entre 1 e 5
                jogadaLinhaPlayer = int(input('Digite o número da linha que deseja atacar o computador (1 a 5): ')) - 1
            jogadaColunaPlayer = int(input('Digite o número da coluna que deseja atacar o computador (1 a 10): ')) - 1
            while jogadaColunaPlayer < 0 or jogadaColunaPlayer >= 10:  # laço para o jogador só digitar entre 1 e 10
                jogadaColunaPlayer = int(input('Digite o número da linha que deseja atacar o computador (1 a 10): ')) - 1

            #  verificação para que o jogador não repita a mesma posição
            if matrizAuxiliar2[jogadaLinhaPlayer][jogadaColunaPlayer] != '❌' and matrizAuxiliar2[jogadaLinhaPlayer][jogadaColunaPlayer] != '🚢':
                if matrizPc[jogadaLinhaPlayer][jogadaColunaPlayer] == 'X':  # verificação para caso ele acertar o navio
                    matrizAuxiliar2[jogadaLinhaPlayer][jogadaColunaPlayer] = '❌'
                    print('\n')
                    print(f'Voce escolheu a linha {jogadaLinhaPlayer + 1}')
                    print(f'Voce escolheu a coluna {jogadaColunaPlayer + 1}')
                    print('Você acertou uma embarcação do Pc, boa!')
                    print('\n')
                    embarcacoesPc -= 1

                    if embarcacoesPc == 0:  # verificação para caso o pc não tiver mais embarcações
                        break
                else:  # else para caso o jogador erre o navio inimigo
                    matrizAuxiliar2[jogadaLinhaPlayer][jogadaColunaPlayer] = '🚢'
                    print('\n')
                    print(f'Voce escolheu a linha {jogadaLinhaPlayer + 1}')
                    print(f'Voce escolheu a coluna {jogadaColunaPlayer + 1}')
                    print('Você não acertou nenhuma embarcação!')
                    print('\n')

        #  sorteio da jogada do pc e verificação para garantir que não repita a posição
        jogadaLinhaPc = random.randint(0, 4)
        jogadaColunaPc = random.randint(0, 9)
        if matrizAuxiliar[jogadaLinhaPc][jogadaColunaPc] != '❌' and matrizAuxiliar[jogadaLinhaPc][jogadaColunaPc] != '🚢':

            if embarcacoesPlayer > 0:  # verificação se o player ainda tem navios

                if matrizJogador[jogadaLinhaPc][jogadaColunaPc] == 'X':  # verificação para caso acertar um navio
                    matrizAuxiliar[jogadaLinhaPc][jogadaColunaPc] = '❌'
                    print(f'Pc escolheu a linha {jogadaLinhaPc}')
                    print(f'Pc escolheu a coluna {jogadaColunaPc}')
                    print('O Pc acertou uma de suas embarcações, cuidado!')
                    print('\n')
                    embarcacoesPlayer -= 1
                else:  # verificação para caso erre a jogada
                    matrizAuxiliar[jogadaLinhaPc][jogadaColunaPc] = '🚢'
                    print(f'Pc escolheu a linha {jogadaLinhaPc}')
                    print(f'Pc escolheu a coluna {jogadaColunaPc}')
                    print('O pc não acertou nenhuma de suas embarcações!')
                    print('\n')

    print('Resultados finais')  # print que exibe o resultado final após um dos dois perder
    for i in range(5):
        print(matrizAuxiliar[i])
    print('\n')
    for j in range(5):
        print(matrizAuxiliar2[j])

    #  verificação de mensagem final dependendo de quem ganhou o jogo
    if embarcacoesPc == 0:
        print('Parabens, você ganhou o jogo!')
    elif embarcacoesPlayer == 0:
        print('Não foi dessa vez, o pc ganhou o jogo!')
    print('Jogo desenvolvido por: Nicolas Lourenço')
    print('Obrigado por jogar!')