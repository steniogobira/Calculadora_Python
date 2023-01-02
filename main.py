from operacoes import *
from time import sleep
import os


while True:
    print('=<'*40)
    print('CALCULADORA DO GOBIS'.center(80))
    print('=<'*40)

    print('MENU DE NAVEGAÇÃO:'.ljust(80))
    print()

    print("0: SOMA")
    print("1: SUBTRAÇÃO")
    print("2: MULTIPLICAÇÃO")
    print("3: DIVISÃO")
    print("4: EXPONENCIAÇÃO")
    print("5: RAIZ QUADRADA")
    print()

    operacao = int(input(
        'Escolha um dos numeros para cada operação do MENU DE NAVEGAÇÃO que deseja realizar: '))
    print()
    print('=<'*40)
    while operacao not in [0, 1, 2, 3, 4, 5]:
        print('Por favor, escolha umas das opções do MENU DE NAVEGAÇÃO')
        print()
        operacao = int(input())
    listaoperacao = ["SOMA", "SUBTRAÇÃO", "MULTIPLICAÇÃO",
                     "DIVISÃO", "EXPONENCIAÇÃO", "RAIZ QUADRADA"]
    listafuncoes = [soma, subtracao, multiplicacao,
                    divisao, exponenciacao, raiz]
    for c in range(6):
        if operacao == c:
            print(F'Operação escolhida =======> {listaoperacao[c]}')
            print('=<'*40)
            listafuncoes[c]()
            print('=<'*40)
    print('Quer fazer outra operação? \n S- Sim \n N- Não')
    navegacao = input().upper()
    while navegacao not in ['S', 'N']:
        print('Por favor, escolha umas das opções')
        navegacao = input().upper()
    if navegacao == "S":
        os.system('clear') or None

    else:
        print('Ok, abraços!')
        sleep(3)
        os.system('clear') or None
        break
