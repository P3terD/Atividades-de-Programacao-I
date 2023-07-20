#Verifica jogadas do Jogo da Velha

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    print(f" {p7} | {p8} | {p9} "
          f"\n---+---+---"
          f"\n {p4} | {p5} | {p6} "
          f"\n---+---+---"
          f"\n {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    c1 = (p1 == " " or p1 == "x" or p1 == "o")
    c2 = (p2 == " " or p2 == "x" or p2 == "o")
    c3 = (p3 == " " or p3 == "x" or p3 == "o")
    c4 = (p4 == " " or p4 == "x" or p4 == "o")
    c5 = (p5 == " " or p5 == "x" or p5 == "o")
    c6 = (p6 == " " or p6 == "x" or p6 == "o")
    c7 = (p7 == " " or p7 == "x" or p7 == "o")
    c8 = (p8 == " " or p8 == "x" or p8 == "o")
    c9 = (p9 == " " or p9 == "x" or p9 == "o")

    return True if (c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and c9) else False

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.
    Retorna True se a jogada for válida e False, caso contrário
    """
    xPlays = 0
    oPlays = 0

    if p1 == "x":
        xPlays += 1
    elif p1 == "o":
        oPlays += 1

    if p2 == "x":
        xPlays += 1
    elif p2 == "o":
        oPlays += 1

    if p3 == "x":
        xPlays += 1
    elif p3 == "o":
        oPlays += 1

    if p4 == "x":
        xPlays += 1
    elif p4 == "o":
        oPlays += 1

    if p5 == "x":
        xPlays += 1
    elif p5 == "o":
        oPlays += 1

    if p6 == "x":
        xPlays += 1
    elif p6 == "o":
        oPlays += 1

    if p7 == "x":
        xPlays += 1
    elif p7 == "o":
        oPlays += 1

    if p8 == "x":
        xPlays += 1
    elif p8 == "o":
        oPlays += 1

    if p9 == "x":
        xPlays += 1
    elif p9 == "o":
        oPlays += 1

    return True if (0 <= abs(xPlays - oPlays) <= 1) else False

def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ("x" ou "o") venceu a jogada. 
    """
    vv1 = (p7 == p4 == p1)
    vv2 = (p8 == p5 == p2)
    vv3 = (p9 == p6 == p3)
    vh1 = (p7 == p8 == p9)
    vh2 = (p4 == p5 == p6)
    vh3 = (p1 == p2 == p3)
    vd1 = (p7 == p5 == p3)
    vd2 = (p9 == p5 == p1)

    if ((vv1 or vh1) and p7 != ' ') or ((vv2 or vh2  or vd1 or vd2) and p5 != ' ') or ((vv3 or vh3) and p3 != ' '):
        if vv1 or vh1:
            print(f"O jogador '{p7}' venceu!")
        elif vv2 or vh2 or vd1 or vd2:
            print(f"O jogador '{p5}' venceu!")
        elif vv3 or vh3:
            print(f"O jogador '{p3}' venceu!")
    elif (p1 != " " and p2 != " " and p3 != " " and p4 != " " and p5 != " " and p6 != " " and p7 != " "
    and p8 != " " and p9 != " "):
        print("Empate!")
    else:
        print("O jogo nao terminou!")

######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
