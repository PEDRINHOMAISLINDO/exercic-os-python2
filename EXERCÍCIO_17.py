# 17) Ler as notas da 1a. e 2a. avaliações de um aluno.
# Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado
# (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

print('==' * 25)
print('MÉDIA DE UM ALUNO: ')
print('==' * 25)
nota1 = float(input('DIGOTE SUA NOTA EM MATEMÁTICA : '))
print('==' * 25)
nota2 = float(input('DIGITE SUA NOTA EM PORTUGUÊS: '))
print('==' * 25)
media = (nota1 + nota2) / 2
if media >= 6:
    print('==' * 25)
    print(f'PARABÉNS!, VOCÊ FOI APROVADO . SUA NOTA FOI {media}')
    print('==' * 25)
else:
    print('==' * 25)
    print(f'INFELIZMENTE, VOCÊ FOI REPROVADO . SUA NOTA FOI DE {media}')
    print('==' * 25)
exit()