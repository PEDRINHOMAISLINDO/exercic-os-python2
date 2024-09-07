#11) Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês
# , mais uma comissão também fixa de R$ 700,00
# para cada carro vendido e mais 5% do valor das vendas por ele efetuadas.
# Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido.
# Calcule e escreva o salário final do vendedor.
from time import sleep
print('=-' * 25)
print('REVENDEDORA: ')
print('=-' * 25)
sleep(2)
saláriofixo = float(input('DIGITE SEU SALÁRIO ATUAL: '))
print('=-' * 25)
carros = int(input('QUANTOS CARROS VOCÊ VENDEU: '))
print('=-' * 25)
vendas = float(input('VALOR DE SUAS VENDAS: ')
print('PROCESSANDO...')
print('=-' * 25)
sleep(2)
# CALCULO DE 700$
calculo = carros * 700
# CALCULO 5%
calculo5 = (vendas * 5) / 100
print(f'''RESULTADOS :
VALOR DE SUAS VENDAS = {vendas}
SEU SALÁRIO = {saláriofixo}
QUANTOS CARROS VENDIDOS = {carros}''')
print('=-' * 25)
print('PROCESSANDO SEU SALÁRIO FINAL...')
sleep(1)
print(f'SEU SALÁRIO FICOU {saláriofixo + calculo5 + calculo}')



