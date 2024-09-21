print('=-' * 25)# MULTIPLICANDO A STR "=-" POR 25
print('ESTOQUE')
print('=-' * 25)
quantidade_atual = int(input('DIGITE A QUANTIDADE ATUAL DO ESTOQUE: '))
print('=-' * 25)
quantidade_minima = int(input('DIGITE A QUANTIDADE MÍNIMA DO ESTOQUE: '))
print('=-' * 25)
quantidade_maxima = int(input('DIGITE A QUANTIDADE MÁXIMA DO ESTOQUE: '))
print('=-' * 25)
quantidade_media = (quantidade_maxima - quantidade_minima) / 2 # CALCULANDO A MÉDIA
print('=-' * 25)

if quantidade_media >= quantidade_atual: # ESTRUTURA DE CONDIÇÃO
     print('NÃO EFETUAR A COMPRA')
else:
    print('EFETUAR A COMPRA')
exit()