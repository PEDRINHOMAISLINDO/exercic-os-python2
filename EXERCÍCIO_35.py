print('==' * 25)
print('POSTO DE GASOLINA')
print('==' * 25)
combustivel = input('ESCOLHA UM COMBUSTÍVEL: GASOLINA OU ALCOOL: ').upper() #  DEIXA OS CARACTÉRES DA VARIÁVEL TODAS  EM MAIÚSCULAS
print('==' * 25)

while combustivel != 'GASOLINA' and combustivel != 'ALCOOL': # ESTRUTURA DE REPETIÇÃO CASO A VAR (COMBUSTIVEL) FOR DIFERENTE DE 'GASOLINA' E 'ALCOOL'
    print('ESCREVA NOVAMENTE!')
    combustivel = input('ESCOLHA UM COMBUSTÍVEL: GASOLINA OU ÁLCOOL: ')


if combustivel == 'GASOLINA': # ESTRUTURA DE CONDICÃO SE A VAR (COMBUSTIVEL) == 'GASOLINA'
    gasolina = 3.30
    litros = float(input('QUANTOS LITROS VOCÊ DESEJA COLOCAR: '))
    print('==' * 25)

    if litros > 20:
        resultado = (gasolina - gasolina * 0.6) * litros
        print(f'VOCÊ DEVE PAGAR R${resultado:.2f} DE GASOLINA')
        print('==' * 25)

    elif litros <= 20:
        resultado = (gasolina - gasolina * 0.4) * litros
        print(f'VOCÊ DEVE PAGAR R${resultado:.2f} DE GASOLINA')
        print('==' * 25)


if combustivel == 'ALCOOL': # ESTRUTURA DE CONDICÃO SE A VAR (COMBUSTIVEL) == ALCOOL
    alcool = 2.90
    litros = float(input('QUANTOS LITROS VOCÊ DESEJA COLOCAR: '))
    print('==' * 25)

    if litros > 20:
        resultado = (alcool - alcool * 0.3) * litros
        print(f'VOCÊ VAI PAGAR R${resultado:.2f} DE ÁLCOOL')
        print('==' * 25)

    elif litros <= 20:
        resultado = (alcool - alcool * 0.5) * litros
        print(f'VOCÊ DEVE PAGAR R${resultado:.2f} DE ÁLCOOL')
        print('==' * 25)
    exit()
exit()




