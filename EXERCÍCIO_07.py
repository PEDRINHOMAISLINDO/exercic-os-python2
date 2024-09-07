#7) Faça um algoritmo que leia a idade de uma pessoa expressa em anos,
# meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
# Considerar ano com 365 dias e mês com 30 dias.

# DIAS DE VIDA:
print('=-' * 25)
print('POR QUANTO TEMPO VOCÊ ESTÁ VIVO')
print('=-' * 25)
diaA = 4
mesA = 9
anoA = 2024
dias = 0
diaN = int(input('QUAL FOI O DIA DO SEU NASCIMENTO: '))
mes = int(input('QUAL FOI O MÊS EM QUE VOCÊ NASCEU (EM NUMERO) :'))
ano = int(input('QUAL ANO VOCÊ NASCEU: '))
calculo1 = diaA - diaN
if diaA < diaN:
    calculo1 = diaN - diaA
calculo2 = (mesA - mes) * 30
if mesA < mes:
    calculo2 = (mes - mesA) * 30
calculo3 = (anoA - ano) * 365
resultado = dias + calculo1 + calculo2 + calculo3
print(f' VOCÊ VIVEU BASICAMENTE {resultado} DIAS .')
exit()