# Máquina Automática

from os import system, name

def clearScreen():
    '''Limpa a tela'''

    if name == 'nt':
        system('cls')
    else:
        system('clear')

def insertMoney(price, rcv20=0, rcv10=0, rcv5=0, rcv2=0, rcv1=0, rcv05=0, payed = 0):
    '''Pede para o usuário inserir o dinheiro cédula por cédula ou moeda por moeda até alcançar o preço do produto'''

    clearScreen()

    try:
        value = float(input(f'''
Você deve pagar: R${price-payed:.2f}

╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║           VALORES ACEITOS             ║
╠ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╣  
║R$20,00                                ║
║R$10,00                                ║
║R$5,00                                 ║
║R$2,00                                 ║
║R$1,00                                 ║
║R$0,50                                 ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝

Insira a cédula ou moeda válida: '''))
        if value == 20 or value == 10 or value == 5 or value == 2 or value == 1 or value == 0.5:
            payed += value

            if value == 20:
                rcv20 += 1
            elif value == 10:
                rcv10 += 1
            elif value == 5:
                rcv5 += 1
            elif value == 2:
                rcv2 += 1
            elif value == 1:
                rcv1 += 1
            elif value == 0.5:
                rcv05 += 1
        else:
            print('Insira um valor que seja aceito')
            input('--> Enter para continuar...')
    except:
        print('Insira um valor válido')
        input('--> Enter para continuar...')

    if payed < price:
        return insertMoney(price, rcv20, rcv10, rcv5, rcv2, rcv1, rcv05, payed)
    else:
        change = payed - price
        return change, rcv20, rcv10, rcv5, rcv2, rcv1, rcv05, payed

def paysChange(change, qt20, qt10, qt5, qt2, qt1, qt05, payed, spnt20=0, spnt10=0, spnt5=0, spnt2=0, spnt1=0, spnt05=0):
    '''Paga o troco para o cliente'''
    noChangeOpt = ''
    if (change - 20) >= 0 and qt20 > 0:
        change -= 20
        qt20 -= 1
        spnt20 += 1
    elif (change - 10) >= 0 and qt10 > 0:
        change -= 10
        qt10 -= 1
        spnt10 += 1
    elif (change - 5) >= 0 and qt5 > 0:
        change -= 5
        qt5 -= 1
        spnt5 += 1
    elif (change - 2) >= 0 and qt2 > 0:
        change -= 2
        qt2 -= 1
        spnt2 += 1
    elif (change - 1) >= 0 and qt1 > 0:
        change -= 1
        qt1 -= 1
        spnt1 += 1
    elif (change - 0.5) >= 0 and qt05 > 0:
        change -= 0.5
        qt05 -= 1
        spnt05 += 1
    else:
        noChangeOpt = input(f'Não temos troco o suficiente, deseja não receber R${change} do seu troco? (s/n): ')

        if noChangeOpt == "N" or noChangeOpt == "n":
            print(f"Seus R${payed:.2f} foram devolvidos")
            input('--> Enter para continuar...')
            return qt20+spnt20, qt10+spnt10, qt5+spnt5, qt2+spnt2, qt1+spnt1, qt05+spnt05, 0

        elif noChangeOpt != "S" and noChangeOpt != "s":
            print("Digite uma opcao valida!")
            input('--> Enter para continuar...')

    if change == 0 or noChangeOpt == "S" or noChangeOpt == "s":
        print('Seu troco:' + '\nR$20.00'*spnt20 + '\nR$10.00'*spnt10 + '\nR$5.00'*spnt5 + '\nR$2.00'*spnt2 + '\nR$1.00'*spnt1 + '\nR$0.50' * spnt05)
        input('--> Enter para continuar...')
        return qt20, qt10, qt5, qt2, qt1, qt05, 1
    else:
        return paysChange(change, qt20, qt10, qt5, qt2, qt1, qt05, payed, spnt20, spnt10, spnt5, spnt2, spnt1, spnt05)

def buyPdct(item, prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income, price1, price2, price3):
    '''Responsável pela compra dos produtos e troco'''
    rcvMoney = 0
    sold1 = 0
    sold2 = 0
    sold3 = 0
    hasProduct = 1

    if item == 1:
        if prod1 < 1:
            hasProduct = 0
            print('O produto \'Batata List\' está em falta')
            input('--> Enter para continuar...')
        else:
            change, rcv20, rcv10, rcv5, rcv2, rcv1, rcv05, payed = insertMoney(price1)
            rcvMoney = price1
            sold1 = 1

    elif item == 2:
        if prod2 < 1:
            hasProduct = 0
            print('O produto \'Suco Py\' está em falta')
            input('--> Enter para continuar...')
        else:
            change, rcv20, rcv10, rcv5, rcv2, rcv1, rcv05, payed = insertMoney(price2)
            rcvMoney = price2
            sold2 = 1

    elif item == 3:
        if prod3 < 1:
            hasProduct = 0
            print('O produto \'Guaraná Lambda\' está em falta')
            input('--> Enter para continuar...')
        else:
            change, rcv20, rcv10, rcv5, rcv2, rcv1, rcv05, payed = insertMoney(price3)
            rcvMoney = price3
            sold3 = 1

    if hasProduct == 1 and change == 0:
        return prod1-sold1, prod2-sold2, prod3-sold3, qt20+rcv20, qt10+rcv10, qt5+rcv5, qt2+rcv2, qt1+rcv1, qt05+rcv05, income+rcvMoney
    elif hasProduct == 1 and change != 0:
        qtAt20, qtAt10, qtAt5, qtAt2, qtAt1, qtAt05, sold = paysChange(change, qt20, qt10, qt5, qt2, qt1, qt05, payed) #recebe a quantidade atualizada das cédulas e se o prouto foi vendido
        return prod1-(sold1*sold), prod2-(sold2*sold), prod3-(sold3*sold), qtAt20+rcv20, qtAt10+rcv10, qtAt5+rcv5, qtAt2+rcv2, qtAt1+rcv1, qtAt05+rcv05, income+(rcvMoney*sold)
    else:
        return prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income

def info(prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income):
    '''Mostra todas as informações internas da loja'''
    clearScreen()

    print(f'''
╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║               PRODUTOS                ║
╠ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╣
║1. Batata List: {prod1}            (\ /)     ║            
║2. Suco Py: {prod2}                 ( ..)    ║
║3. Guaraná Lambda: {prod3}          c(")(")  ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝

╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║                 NOTAS                 ║
╠ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╣  
║R$20,00: {qt20}                             ║
║R$10,00: {qt10}                             ║
║R$5,00: {qt5}                              ║
║R$2,00: {qt2}                              ║
║R$1,00: {qt1}                              ║
║R$0,50: {qt05}                              ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝

╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═
║Faturamento: R${income:.2f}                         
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ 

''')
    input('--> Enter para continuar...')

def main(prod1=3, prod2=3, prod3=3, qt20=5, qt10=5, qt5=5, qt2=5, qt1=5, qt05=5, income=0.00, ext=0):
    clearScreen()

    price1 = 3.00
    price2 = 2.50
    price3 = 4.50

    try:
        opt = int(input(f'''
╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║               PRODUTOS                ║
╠ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╣
║1. Batata List.....R${price1:.2f}    (\ /)     ║            
║2. Suco Py.........R${price2:.2f}     ( ..)    ║
║3. Guaraná Lambda..R${price3:.2f}     c(")(")  ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝

╔ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╗
║             OUTRAS OPÇÕES             ║
╠ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╣  
║4. Informações Internas                ║     
║5. Finalizar                           ║
╚ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ╝

Digite o(a) produto/opcao desejado(a): '''))

        if opt == 1 or opt == 2 or opt == 3:
            prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income = buyPdct(opt, prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income, price1, price2, price3)
        elif opt == 4:
            info(prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income)
        elif opt == 5:
            ext = 1
        else:
            print('Escolha uma opcao valida')
            input('--> Enter para continuar...')

    except:
        print("Você deve digitar um valor inteiro")
        input('--> Enter para continuar...')

    if ext == 0:
        return main(prod1, prod2, prod3, qt20, qt10, qt5, qt2, qt1, qt05, income)
    else:
        return print('Aguardamos sua proxima visita :D')

main()
