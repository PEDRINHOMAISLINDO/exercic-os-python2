# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias
# e escreva a idade dessa pessoa expressa apenas em dias.
# Considerar ano com 365 dias e mês com 30 dias.
#QUANTOS DIAS VOCÊ ESTÁ VIVO:

# DIAS DE VIDA:
diaA = 29
mesA = 8
anoA = 2024
dia = 0
diaN = int(input('EM QUE DIA VOCE NASCEU: '))
mesN = int(input('EM QUE MES VOCE NASCEU: '))
anoN = int(input('EM QUE ANO VOCE NASCEU: '))
calculo = diaA - diaN
if diaA < diaN:
    calculo = diaN - diaA
calculo2 = (mesA - mesN) * 30
if mesA < mesN:
    calculo2 = (mesN - mesA) * 30
calculo3 = (anoA - anoN) * 365
if anoA < anoN:
    calculo3 = (anoN - anoA) * 365
print(f'SEUS DIAS DE VIDA NA TERRA É DE {dia + calculo + calculo2 + calculo3}')












