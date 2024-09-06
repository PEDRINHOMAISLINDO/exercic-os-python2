# 18) Ler o ano atual e o ano de nascimento de uma pessoa.
# Escrever uma mensagem que diga se ela poderá ou não votar este ano
# (não é necessário considerar o mês em que a pessoa nasceu).

print('==' * 25)
print('IDADE PARA VOTAR: ')
print('==' * 25)
ano = int(input('DIGA O ANO EM QUE VOCÊ NASCEU: '))
print('==' * 25)
if 2024 - ano > 16:
    print('==' * 25)
    print('VOCÊ PODERÁ VOTAR')
    print('==' * 25)
else:
    print('==' * 25)
    print('VOCÊ NÃO PODE VOTAR')
    print('==' * 25)
exit()