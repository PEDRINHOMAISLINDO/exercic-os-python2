print('=-' * 25)
print('HORAS EXTRAS')
print('=-' * 25)
trabalho = float(input('QUANTO VOCÊ RECEBE: '))
print('=-' * 25)
horatraba1 = float(input('QUANTAS HORAS VOCÊ TRABALHOU NA PRIMEIRA SEMANA: '))
print('=-' * 25)
horatraba2 = float(input('QUANTAS HORAS VOCÊ TRABALHOU NA SEGUNDA SEMANA: '))
print('=-' * 25)
horatraba3 = float(input('QUANTAS HORAS VOCÊ TRABALHOU NA TERCEIRA SEMANA: '))
print('=-' * 25)
horatraba4 = float(input('QUANTAS HORAS VOCÊ TRABALHOU NA QUARTA SEMANA: '))
print('=-' * 25)
horamensal = horatraba1 + horatraba4 + horatraba3 + horatraba2
semanalmente = trabalho / 4
calculohora = trabalho / 220

if horatraba1 >= 40:
    calculo1 = (horatraba1 - 40) * calculohora + (horatraba1 - 40) * calculohora / 2
else:
    calculo1 = (semanalmente / 60) * calculohora


if horatraba2 >= 40:
    calculo2 = (horatraba2 - 40) * calculohora + (horatraba2 - 40) * calculohora / 2
else:
    calculo2 = (semanalmente / 60) * calculohora


if horatraba3 >= 40:
    calculo3 = (horatraba3 - 40) * calculohora + (horatraba3 - 40) * calculohora / 2
else:
    calculo3 = (semanalmente / 60) * calculohora


if horatraba4 >= 40:
    calculo4 = (horatraba4 - 40) * calculohora + (horatraba4 - 40) * calculohora / 2
else:
    calculo4 = (semanalmente / 60) * calculohora


total = trabalho + calculo1 + calculo2 + calculo3 + calculo4
print(f'VOCÊ TRABALHOU EXATAMENTE {horamensal:.0f} HORAS EM 1 MÊS, E SEU SALÁRIO TOTAL FOI DE R${total:.2f}')
exit()



