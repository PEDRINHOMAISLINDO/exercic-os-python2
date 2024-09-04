# calculadora:
from time import sleep
from colorama import init, Fore
init()
#inicialização do programa
print(Fore.LIGHTWHITE_EX + 'TABUADA ESTÁCIO INICIANDO...')
sleep(2)
numero = int(input(Fore.LIGHTMAGENTA_EX + 'ESCOLHA UM NÚMERO (1), (2), (3): '))
if numero == 1:
    # ESTRUTURA CONDICIONAL PARA ESCOLHA DE OPERADORES ARITMÉTICOS:
    print(Fore.LIGHTRED_EX + '=-' * 25)
    numero1 = int(input(Fore.LIGHTMAGENTA_EX + 'ESCOLHA UM NÚMERO DE 1 ATÉ 10: '))
    print(Fore.LIGHTRED_EX + '=-' * 25)
    operador = input(Fore.LIGHTMAGENTA_EX + 'ESCOLHA UM OPERADOR ARTMÉTICO +, -, x, /: ')
    print(Fore.GREEN + '=-' * 25)
    if operador == '+':
        for c in range(11):
            print((f'{numero1} + {c} = {numero1 + c}'))
    elif operador == '-':
        for c in range(11):
            print(f'{c + numero1} - {c} = {(c + numero1) - c}')
    elif operador == 'x':
        for c in range(11):
            print(f'{numero1} x {c} = {numero1 * c}')
    elif operador == '/':
        for c in range(11):
            print(f'{c * numero1} : {numero1} = { (c * numero1) / numero1:.0f}')
if numero == 2:
    #TABUADA COMPLETA:
    print(Fore.YELLOW + 'INICIANDO OPÇÃO DE TABUADA COMPLETA...')
    sleep(2)
    print(Fore.LIGHTRED_EX + '=-' * 25)
    numero1 = int(input('ESCOLHA UM NUMERO DE 1 ATÉ 10: '))
    print(Fore.LIGHTRED_EX + '=-' * 25)
    for c in range(1, 11):
        print(f'''{numero1} + {c} = {numero1 + c} / /  {c + numero1} - {numero1} = {(c + numero1) - numero1} / / {numero1} x {c} = {numero1 * c} / / {numero1 * c} : {numero1} = {(numero1 * c) / numero1:.0f}''' )
if numero == 3:
    #ENCERRAMENTO DO PROGRAMA
    print(Fore.LIGHTMAGENTA_EX + 'PROGRAMA ENCERRANDO...')
    sleep(2)
    exit()




