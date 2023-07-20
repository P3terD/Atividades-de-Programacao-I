# Desenha formas geométricas

def draw(obj, altura, largura, simb, i=1):
    ### Retângulo ###
    if obj == "R":
        if i == 1 or i == altura:
            print(simb*largura)
        else:
            print(simb + ((" "*abs(largura-2)) if largura > 2 else "") + (simb if largura >= 2 else ""))

    ### Paralelogramo ###
    elif obj == "P":
        if i == 1:
            print(simb*largura)
        elif i == altura:
            print(" "*(altura-1) + simb*largura)
        else:
            print(" " * (i - 1) + simb + ((" "*abs(largura-2)) if largura > 2 else "") + (simb if largura >= 2 else ""))

    ### Triângulo Equilátero ###
    elif obj == "TE":
        if i == 1:
            print(" "*(altura-i) + simb)
        elif i == altura:
            print(simb*(1 + 2*(i-1)))
        else:
            print(" "*(altura-i) + simb + " "*(-1 + 2*(i-1)) + (simb if i != 1 else ""))

    ### Triângulo Retângulo Esquerdo ###
    elif obj == "TRE":
        if i == 1:
            print(simb)
        elif i == altura:
            print(simb*altura)
        else:
            print(simb + " "*(i-2) + simb)

    ### Triângulo Retângulo Direito ###
    elif obj == "TRD":
        if i == 1:
            print(" "*(altura-1) + simb)
        elif i == altura:
            print(simb * altura)
        else:
            print(" "*(altura-i) + simb + " "*(i-2) + simb)

    ### Repetição da Função ###
    if i < altura:
        i += 1
        draw(obj, altura, largura, simb, i)

def main():
    obj = input()
    largura = 1

    if obj == "R" or obj == "P":
        largura = int(input())
        altura = int(input())
    elif obj == "TE" or obj == "TRE" or obj == "TRD":
        altura = int(input())

    simb = input()

    if obj != "R" and obj !="P" and obj != "TE" and obj != "TRE" and obj != "TRD":
         return print("Objeto invalido.")

    if altura < 1 or largura < 1:
        return print("Medida invalida.")

    draw(obj, altura, largura, simb)
main()
