# calculadora:
numero = int(input('Escolha um número (1), (2), (3): '))
if numero == 1:
    # ESTRUTURA CONDICIONAL PARA ESCOLHA DE OPERADORES ARITMÉTICOS:
    numero1 = int(input('ESCOLHA UM NUMERO DE 1 ATÉ 10: '))
    operador = input('ESCOLHA UM OPERADOR ARTMÉTICO +, -, *, /: ')
    if operador == '+':
        for c in range(11):
            print((f'{numero1}{operador}{c} = {numero1 + c}'))
    if operador == '-':
        for c in range(11):
            print(f'{numero1}{operador}{c} = {numero1 - c}')
    if operador == 'x':
        for c in range(11):
            print(f'{numero1}{operador}{c} = {numero1 * c}')
    if operador == '/':
        for c in range(10):
            print(f'{c * numero1}{operador}{numero1} = { numero1 / c:.0f}')
if numero == 2:
    #TABUADA COMPLETA:
    numero1 = int(input('ESCOLHA UM NUMERO DE 1 ATÉ 10: '))
    operador = input('ESCOLHA UM OPERADOR ARTMÉTICO +, -, *, /: ')
    #if operador == '+':
       # for c in range(11):
