#Jogo da velha

import random
from os import system, name

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 
                
def atualizaTabuleiro(tabuleiro, posicao = 0, simbolo = 0, acabou=0):
    """
    Função utilizada para atualizar a lista do tabuleiro

    Parâmetros:
    tabuleiro: lista que armazena as posições do tabuleiro
    posicao: posição onde se deseja jogar
    simbolo: simbolo do jogador
    acabou: 1 se o jogo já acabou, 0 se não

    Saída:
    0 se a posição já se encontra ocupada, se não, retorna a lista atualizada com as novas posições do tabuleiro
    """
    if tabuleiro[posicao] == posicao or acabou == 1:
        tabuleiro[posicao] = simbolo
    else:
        return 0
    return tabuleiro
                
def desenhaTabuleiro(tabuleiro):
    """
    Função utilizada para desenhar o tabuleiro

    Parâmetros:
    tabuleiro: lista que armazena as posições do tabuleiro
    """
    limpaTela()
    print(f'''
\033[0;37;45m  tictactoe.app  \033[m
\033[0;37m▌\033[m               \033[0;37m▐\033[m
\033[0;37m▌\033[m   {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]}   \033[0;37m▐\033[m
\033[0;37m▌\033[m  ---+---+---  \033[0;37m▐\033[m     (\ /) 
\033[0;37m▌\033[m   {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]}   \033[0;37m▐\033[m      ( ..) 
\033[0;37m▌\033[m  ---+---+---  \033[0;37m▐\033[m      c(")(")
\033[0;37m▌\033[m   {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]}   \033[0;37m▐\033[m
\033[0;37m▌\033[m               \033[0;37m▐\033[m
\033[0;37m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[m''')
                
def escolheLetra():
    """
    Função utilizada para um dos jogadores escolher qual letra quer usar

    Retorno:
    Letra (X ou O) escolhida pelo jogador
    """
    letraEscolhida = input("Você quer ser o jogador \'X\' ou o jogador \'O\'? ")

    if letraEscolhida == "X":
        jogador = 'X'
        maquina = 'O'
    elif letraEscolhida == "O": 
        jogador = 'O'
        maquina = 'X'
    else:
        print('Digite uma opção válida!')
        input('--> Enter para continuar...')
        return escolheLetra()

    return jogador, maquina

def jogadaJogador(tabuleiro):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do jogador e pergunta ao jogador onde quer jogar
    O tabuleiro pode estar vazio (caso o jogador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista que armazena as posições do tabuleiro

    Retorno:
    Posição (entre 1 e 9) da jogada do jogador
    """
    try: 
        jogada = int(input("Escolha a posição onde deseja jogar: "))
        if 0 < jogada < 10:
            if tabuleiro[jogada] == jogada:
                return jogada
            else:
                print('Posição já se encontra ocupada!')
                input('--> Enter para continuar...')
                return jogadaJogador(tabuleiro[:])
        else: 
            print('Digite uma opção válida!')
            input('--> Enter para continuar...')
            return jogadaJogador(tabuleiro[:])
    except:
        print('Digite um número inteiro!')
        input('--> Enter para continuar...')
        return jogadaJogador(tabuleiro[:])

def jogadaComputador(tabuleiro, simboloComputador, dificuldade = 2):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista que armazena as posições do tabuleiro
    simboloComputador: letra do computador 
    dificuldade: dificuldade do computador escolhida pelo player

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia: 
    A estratégia é o computador sempre começar no meio e utilizar padrões de ataque, garantindo que nunca perderá
    """
    if dificuldade == 1:
        jogada = random.randint(1, 9)
        if tabuleiro[jogada] == jogada:
            return jogada
        else:
            return jogadaComputador(tabuleiro[:], simboloComputador, dificuldade)
        
    elif dificuldade == 2:
        ### CHECA SE O BOT PODE GANHAR 
        if ((tabuleiro[2] == tabuleiro[3] == simboloComputador) or (tabuleiro[5] == tabuleiro[9] == simboloComputador) or (tabuleiro[4] == tabuleiro[7] == simboloComputador)) and tabuleiro[1] == 1:
            return 1
        elif ((tabuleiro[1] == tabuleiro[3] == simboloComputador) or (tabuleiro[5] == tabuleiro[8] == simboloComputador)) and tabuleiro[2] == 2:
            return 2
        elif ((tabuleiro[1] == tabuleiro[2] == simboloComputador) or (tabuleiro[5] == tabuleiro[7] == simboloComputador) or (tabuleiro[6] == tabuleiro[9] == simboloComputador)) and tabuleiro[3] == 3:
            return 3
        elif ((tabuleiro[7] == tabuleiro[1] == simboloComputador) or (tabuleiro[5] == tabuleiro[6] == simboloComputador)) and tabuleiro[4] == 4:
            return 4
        elif ((tabuleiro[4] == tabuleiro[6] == simboloComputador) or (tabuleiro[2] == tabuleiro[8] == simboloComputador) or (tabuleiro[1] == tabuleiro[9] == simboloComputador)
              or (tabuleiro[3] == tabuleiro[7] == simboloComputador)) and tabuleiro[5] == 5:
            return 5
        elif ((tabuleiro[4] == tabuleiro[5] == simboloComputador) or (tabuleiro[3] == tabuleiro[9] == simboloComputador)) and tabuleiro[6] == 6:
            return 6
        elif ((tabuleiro[4] == tabuleiro[1] == simboloComputador) or (tabuleiro[8] == tabuleiro[9] == simboloComputador) or (tabuleiro[5] == tabuleiro[3] == simboloComputador)) and tabuleiro[7] == 7:
            return 7
        elif ((tabuleiro[7] == tabuleiro[9] == simboloComputador) or (tabuleiro[5] == tabuleiro[2] == simboloComputador)) and tabuleiro[8] == 8:
            return 8
        elif ((tabuleiro[7] == tabuleiro[8] == simboloComputador) or (tabuleiro[5] == tabuleiro[1] == simboloComputador) or (tabuleiro[6] == tabuleiro[3] == simboloComputador)) and tabuleiro[9] == 9:
            return 9
        
        #CHECA SE O JOGADOR VAI GANHAR
        elif ((tabuleiro[2] == tabuleiro[3]) or (tabuleiro[5] == tabuleiro[9]) or (tabuleiro[4] == tabuleiro[7])) and tabuleiro[1] == 1:
            return 1
        elif ((tabuleiro[1] == tabuleiro[3]) or (tabuleiro[5] == tabuleiro[8])) and tabuleiro[2] == 2:
            return 2
        elif ((tabuleiro[1] == tabuleiro[2]) or (tabuleiro[5] == tabuleiro[7]) or (tabuleiro[6] == tabuleiro[9])) and tabuleiro[3] == 3:
            return 3
        elif ((tabuleiro[7] == tabuleiro[1] ) or (tabuleiro[5] == tabuleiro[6])) and tabuleiro[4] == 4:
            return 4
        elif ((tabuleiro[4] == tabuleiro[6]) or (tabuleiro[2] == tabuleiro[8]) or (tabuleiro[1] == tabuleiro[9])
              or (tabuleiro[3] == tabuleiro[7])) and tabuleiro[5] == 5:
            return 5
        elif ((tabuleiro[4] == tabuleiro[5]) or (tabuleiro[3] == tabuleiro[9])) and tabuleiro[6] == 6:
            return 6
        elif ((tabuleiro[4] == tabuleiro[1]) or (tabuleiro[8] == tabuleiro[9]) or (tabuleiro[5] == tabuleiro[3])) and tabuleiro[7] == 7:
            return 7
        elif ((tabuleiro[7] == tabuleiro[9]) or (tabuleiro[5] == tabuleiro[2])) and tabuleiro[8] == 8:
            return 8
        elif ((tabuleiro[7] == tabuleiro[8]) or (tabuleiro[5] == tabuleiro[1]) or (tabuleiro[6] == tabuleiro[3])) and tabuleiro[9] == 9:
            return 9
        
        #JOGA NORMALMENTE SE NINGUÉM ESTIVER PARA GANHAR
        else:
            if tabuleiro[5] == 5:
                return 5
            else:
                if tabuleiro[9] == 9:
                    return 9
                else:
                    if tabuleiro[7] == 7:
                        return 7
                    else:
                        if tabuleiro[1] == 1:
                            return 1
                        else:
                            if tabuleiro[3] == 3:
                                return 3
                            else:
                                jogada = random.randint(1, 9)
                                if tabuleiro[jogada] == jogada:
                                    return jogada
                                else:
                                    return jogadaComputador(tabuleiro[:], simboloComputador, dificuldade)
            

def checaJogo(tabuleiro):
    """
    Função que checa se o jogo já terminou ou não

    Parâmetros:
    tabuleiro: lista que armazena as posições do tabuleiro

    Retorno:
    0 se o jogo não tiver terminado; 
    1 se o ganhador for o X; 
    2 se o ganhador for o O; 
    3 se houve um empate; 
    """ 
    ganhador = ""

    if tabuleiro[1] == tabuleiro[2] == tabuleiro[3]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 1, f"\033[0;31m{tabuleiro[1]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 2, f"\033[0;31m{tabuleiro[2]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 3, f"\033[0;31m{tabuleiro[3]}\033[m", 1)
        ganhador = tabuleiro[1]
    elif tabuleiro[4] == tabuleiro[5] == tabuleiro[6]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 4, f"\033[0;31m{tabuleiro[4]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 5, f"\033[0;31m{tabuleiro[5]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 6, f"\033[0;31m{tabuleiro[6]}\033[m", 1)
        ganhador = tabuleiro[4]
    elif tabuleiro[7] == tabuleiro[8] == tabuleiro[9]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 7, f"\033[0;31m{tabuleiro[7]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 8, f"\033[0;31m{tabuleiro[8]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 9, f"\033[0;31m{tabuleiro[9]}\033[m", 1)
        ganhador = tabuleiro[9]
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 1, f"\033[0;31m{tabuleiro[1]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 4, f"\033[0;31m{tabuleiro[4]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 7, f"\033[0;31m{tabuleiro[7]}\033[m", 1)
        ganhador = tabuleiro[1]
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 2, f"\033[0;31m{tabuleiro[2]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 5, f"\033[0;31m{tabuleiro[5]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 8, f"\033[0;31m{tabuleiro[8]}\033[m", 1)
        ganhador = tabuleiro[2]
    elif tabuleiro[3] == tabuleiro[6] == tabuleiro[9]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 3, f"\033[0;31m{tabuleiro[3]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 6, f"\033[0;31m{tabuleiro[6]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 9, f"\033[0;31m{tabuleiro[9]}\033[m", 1)
        ganhador = tabuleiro[9]
    elif tabuleiro[1] == tabuleiro[5] == tabuleiro[9]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 1, f"\033[0;31m{tabuleiro[1]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 5, f"\033[0;31m{tabuleiro[5]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 9, f"\033[0;31m{tabuleiro[9]}\033[m", 1)
        ganhador = tabuleiro[1]
    elif tabuleiro[3] == tabuleiro[5] == tabuleiro[7]:
        tabuleiro = atualizaTabuleiro(tabuleiro, 3, f"\033[0;31m{tabuleiro[3]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 5, f"\033[0;31m{tabuleiro[5]}\033[m", 1)
        tabuleiro = atualizaTabuleiro(tabuleiro, 7, f"\033[0;31m{tabuleiro[7]}\033[m", 1)
        ganhador = tabuleiro[3]
    elif (tabuleiro[1] != 1 and tabuleiro[2] != 2 and tabuleiro[3] != 3 and tabuleiro[4] != 4 and tabuleiro[5] != 5 and tabuleiro[6] != 6 and
          tabuleiro[7] != 7 and tabuleiro[8] != 8 and tabuleiro[9] != 9):
        return 3, tabuleiro
    else:
        return 0, tabuleiro
    saida = 1 if ganhador == f"\033[0;31mX\033[m" else 2
    return saida, tabuleiro

def jogar(simboloJogador1, simboloJogador2, tabuleiro, opt, jogada, maqComeca=0):
    """
    Função responsável pelo jogo em si

    Parâmetros:
    simboloJogador1: Símbolo do primeiro jogador
    simboloJogador2: Símbolo do segundo jogador
    tabuleiro: lista que armazena as posições do tabuleiro
    opt: opção de modo escolhid pelo jogador
    jogada: em qual jogada o jogo se encontra
    maqComeca: 1 se a máquina começar, 0 se não
    """ 
    desenhaTabuleiro(tabuleiro[:])
    if opt == 3:
        jogadaNova = jogadaJogador(tabuleiro[:]) if jogada%2 == 1 else jogadaJogador(tabuleiro[:])
        simboloJogada = simboloJogador1 if jogada % 2 == 1 else simboloJogador2

    elif opt == 1 or opt == 2:
        if maqComeca == 1:
            jogadaNova = jogadaComputador(tabuleiro[:], simboloJogador1, opt) if jogada % 2 == 1 else jogadaJogador(tabuleiro[:])
            simboloJogada = simboloJogador1 if jogada % 2 == 1 else simboloJogador2
        else: 
            jogadaNova = jogadaComputador(tabuleiro[:], simboloJogador2, opt) if jogada % 2 == 0 else jogadaJogador(tabuleiro[:])
            simboloJogada = simboloJogador2 if jogada % 2 == 0 else simboloJogador1

    tabuleiro = atualizaTabuleiro(tabuleiro[:], jogadaNova, simboloJogada)
    saida, tabuleiro = checaJogo(tabuleiro[:])

    if saida == 0:
        return jogar(simboloJogador1, simboloJogador2, tabuleiro[:], opt, jogada+1, maqComeca)
    elif saida == 3:
        desenhaTabuleiro(tabuleiro)
        print("Foi um empate!!!")
        input('--> Enter para continuar...')
    else: 
        desenhaTabuleiro(tabuleiro)
        ganhador = "X" if saida == 1 else "O"
        print(f"O jogador {ganhador} ganhou!!!")
        input('--> Enter para continuar...')


def main(ext=0):
    limpaTela()
    try:
        opt = int(input(f'''
\033[0;37;45m  tictactoe.app  \033[m
\033[0;37m▌\033[m               \033[0;37m▐\033[m
\033[0;37m▌\033[m   T | I | C   \033[0;37m▐\033[m     
\033[0;37m▌\033[m  ---+---+---  \033[0;37m▐\033[m     (\ /) 
\033[0;37m▌\033[m   T | A | C   \033[0;37m▐\033[m      ( ..) 
\033[0;37m▌\033[m  ---+---+---  \033[0;37m▐\033[m      c(")(")
\033[0;37m▌\033[m   T | O | E   \033[0;37m▐\033[m
\033[0;37m▌\033[m               \033[0;37m▐\033[m
\033[0;37m▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀\033[m
          
╔══════════════════════╗
║        OPÇÕES        ║
╠ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣  
║1. Facil              ║     
║2. Impossivel         ║
║3. Jogador x Jogador  ║                     
║4. Finalizar          ║       
╚══════════════════════╝
                        
Escolha sua opcao: '''))
        
        if opt == 1 or opt == 2 or opt == 3:
            jogador1, jogador2 = escolheLetra()
            tabuleiro = atualizaTabuleiro(list(range(0,10)))

            limpaTela()
            print("Vamos decidir quem começa no cara ou coroa!!")
            moedaOpt = int(input(f'''Jogador {jogador1}, você quer:
[0] Cara
[1] Coroa
                  
Opção: '''))
            
            limpaTela()
            print('''
⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠠⠤⠤⠤⠶⠶⠤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⢊⣡⣶⣿⡷⠀⠀⠀⣀⣠⣤⣤⣤⣄⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⠿⠟⠋⠀⠀⠀⣾⠉⠀⠀⠀⣀⣤⠞⢴⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠒⠚⠛⠉⠁⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣷⣶⣶⡄⠀⢸⣿⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣉⠉⠉⠀⠀⠀⠻⣿⣿⣷⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠿⠿⢿⠆⢶⣦⣄⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣶⣶⣦⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣬⣉⣉⣛⠀⢸⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠿⠟⠁⢸⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⠾⠿⠿⢿⣿⣿⣿⣿⣿⣿⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠁⠀
            ''')
            input('--> Enter para continuar...')
            moeda = random.randint(0, 1)
            
            limpaTela()
            if moeda == 0:
                print('''
    ▓▓▓▓▓▓▓▓
  ▓▓░░      ▓▓
▓▓░░░░░░░░░░  ▓▓
▓▓░░░░░░░░  ░░▓▓
▓▓░░░░░░░░  ░░▓▓
▓▓░░░░    ░░░░▓▓
  ▓▓░░░░░░░░▓▓
    ▓▓▓▓▓▓▓▓

O resultado é cara!!''')
            else:
                print('''
    ▓▓▓▓▓▓▓▓
  ▓▓      ░░▓▓
▓▓░  ░░░░░░░░░▓▓
▓▓░░░  ░░░░░░░▓▓
▓▓░░░  ░░░░░░░▓▓
▓▓░░░░░   ░░░░▓▓
  ▓▓░░░░░░░░▓▓
    ▓▓▓▓▓▓▓▓
                
O resultado é coroa!!''')
                
            if moedaOpt == moeda:
                print(f"O jogador {jogador1} começa!!")
                input('--> Enter para continuar...')
                jogar(jogador1, jogador2, tabuleiro[:], opt, 1)
            else:
                print(f"O jogador {jogador2} começa!!")
                input('--> Enter para continuar...')
                jogar(jogador2, jogador1, tabuleiro[:], opt, 1, 1)

        elif opt == 4:
            ext = 1
        else: 
            print('Escolha uma opcao valida')
            input('--> Enter para continuar...')
    except Exception as error:
        print(error) 
        print("Você deve digitar um valor inteiro")
        input('--> Enter para continuar...')

    if ext == 0: 
        return main()
    else:
        return print('Espero você me chamar para jogar mais vezes :D')


################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
