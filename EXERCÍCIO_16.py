# 16) As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
# e R$ 1,00 se forem compradas pelo menos 12.
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print('==' * 25)
print('COMPRA DE MAÇAS: ')
print('==' * 25)
maca = int(input('VOCÊ DESEJA QUANTAS MAÇAS ? '))
print('==' * 25)
if maca >= 12:
    preco = maca * 1
    print('==' * 25)
    print(f'SUA COMPRA CUSTOU R${preco}')
    print('==' * 25)
else:
    preco = maca * 1.30
    print('==' * 25)
    print(f'SUAS COMPRA CUSTOU R${preco}')
    print('==' * 25)
exit()
