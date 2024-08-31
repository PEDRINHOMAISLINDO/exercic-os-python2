# Escreva um algoritmo para ler o número total de eleitores de um município,
# o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitor

from time import sleep
#PORCENTAGEM DE ELEITORES
print('=-' * 25)
municipio = input('INFORME O MUNICÍPIO: ')
print("=-" * 25)
print('PROCESSANDO...')
sleep(2)
brancos = int(input('VOTOS BRANCOS: '))
print("=-" * 25)
nulos = int(input(' VOTOS NULOS: '))
print("=-" * 25)
VALIDOS = int(input('VOTOS VÁLIDOS: '))
print("=-" * 25)
totaleleitores = brancos + nulos + VALIDOS
print('PROCESSANDO...')
sleep(2)
print(f'''O PERCENTUAL DE CADA VOTO É
{(brancos * 100) / totaleleitores:.2f}% BRANCOS 
{(nulos * 100) / totaleleitores:.2f}% NULOS 
{(VALIDOS * 100) / totaleleitores:.2f}% VALIDOS ''')
