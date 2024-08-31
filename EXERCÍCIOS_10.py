#10) custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica).
# Supondo que o percentual do distribuidor seja de 28% e os impostos de 45%,
# escrever um algoritmo para ler o custo de fábrica de um carro, calcular e escrever o custo final ao consumidor.


# CUSTO DE CARRO

print('=-' * 25)
custo = float(input('DIGITE O CUSTO DE FABRICA DO CARRO: '))
print('=-' * 25)
distribuidor = custo * 28 / 100
impostos = custo * 45 / 100
resultado = distribuidor + impostos + custo
print('=-' * 25)
print(f'O CARRO PARA O CONSUMIDOR FINAL VAI FICAR COM O PREÇO DE {resultado}')
print('=-' * 25)
exit()

