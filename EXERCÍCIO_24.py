print('=-' * 25)
print('SALÁRIO TOTAL:')
print('=-' * 25)
salario = float(input('QUAL SEU SALÁRIO FIXO: '))
print('=-' * 25)
vendas = float(input('QUANTO VOCÊ VENDEU: '))
print('=-' * 25)
if vendas <= 1500:
    calculo = vendas * 0.03 + salario
    print(f'O TOTAL DO SEU SALÁRIO É DE R${calculo:.2f}')
    print('=-' * 25)
else:
    calculo = vendas * 0.05 + salario
    print(f'O TOTAL DO SEU SALÁRIO É DE R${calculo:.2f}')
    print('=-' * 25)
exit()