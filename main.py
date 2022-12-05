from operacoes import *
from time import sleep
import os


def menu():

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
        operacao = int(input(
            'Escolha um dos numeros para cada operação do MENU DE NAVEGAÇÃO que deseja realizar: '))

    if operacao == 0:
        print('Operação escolhida =======> SOMA')
        print('=<'*40)
        soma()
        print('=<'*40)
    elif operacao == 1:
        print('Operação escolhida =======> SUBTRAÇÃO')
        print('=<'*40)
        subtracao()
        print('=<'*40)
    elif operacao == 2:
        print('Operação escolhida =======> MULTIPLICAÇÃO')
        print('=<'*40)
        multiplicao()
        print('=<'*40)
    elif operacao == 3:
        print('Operação escolhida =======> DIVISÃO')
        print('=<'*40)
        divisao()
        print('=<'*40)
    elif operacao == 4:
        print('Operação escolhida =======> EXPONENCIAÇÃO')
        print('=<'*40)
        exponenciacao()
        print('=<'*40)
    elif operacao == 5:
        print('Operação escolhida =======> RAIZ QUADRADA')
        print('=<'*40)
        raiz()
        print('=<'*40)


menu()
sleep(1)

print('Quer fazer outra operação? \n S- Sim \n N- Não')
navegacao = input().upper()
while navegacao not in ['S', 'N']:
    print('Por favor, escolha umas das opções')
    navegacao = input().upper()
sleep(1)
if navegacao == "S":
    os.system('cls') or None
    menu()
elif navegacao == "N":
    print('Ok, abraços!')
    sleep(3)
    os.system('cls') or None
    exit()
