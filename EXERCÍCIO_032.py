print('<>'* 25 )
print('CONFRONTO ENTRE DOIS TIMES')
print('<>'* 25 )
time_a = input('DIGITE O NOME DO TIME A: ')
print('<>'* 25 )
time_b = input('DIGITE O NOME DO TIME B: ')
print('<>'* 25 )
gols_time_a = int(input(f'QUANTOS GOLS FEZ O {time_a} : '))
print('<>'* 25 )
gols_time_b = int(input(f'QUANTOS GOLS FEZ O {time_b} : '))
print('<>'* 25 )

if gols_time_a > gols_time_b:
    print(f'O {time_a} FOI O GRANDE CAMPEÃO!!!')
    print('<>'* 25 )
else:
    print(f'O {time_b} FOI O GRANDE CAMPEÃO!!!')
    print('<>'* 25 )
if gols_time_a == gols_time_b:
    print(f'O JOGO ENTRE {time_a} E {time_b} DEU EMPATE!!!')
    print('<>'* 25 )
exit()


