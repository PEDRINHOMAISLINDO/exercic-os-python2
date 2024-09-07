# 13) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5.
# Fórmula para o cálculo da média final é:

from time import sleep
print('=-' * 25)
print('MEDIA DO ALUNO: ')
print('=-' * 25)
print('INICIANDO...')
sleep(3)
matematica = float(input('DIGITE SUA NOTA EM MATEMÁTICA'))
print('=-' * 25)
portugues = float(input('DIGITE SUA NOTA EM PORTUGUÊS: '))
print('=-' * 25)
ciencia = float(input('DIGITE SUA NOTA EM CIÊNCIAS: '))
print('=-' * 25)
print('PROCESSANDO...')
sleep(2)
media = (matematica * 2 + portugues * 3 + ciencia * 5) / 10
print(f'SUA MÉDIA É DE {media:.1f}')
print('=-' * 25)
exit()
