print('==' * 25)
print('DUREAÇÃO DE UMA PARTIDA')
print('==' * 25)
inicio = int(input('QUE HORAS A PARTIDA COMEÇOU: '))
fim = int(input('QUE HORAS A PARTIDA TERMINOU: '))
calculo = inicio - fim
if inicio < fim:
    calculo = fim - inicio
while calculo > 24:
    print('UMA PARTIDA NÃO PODE SER MAIS DO QUE 24H.')
    print('POR FAVOR, DIGITE AS HORAS NOVAMENTE')
    print('==' * 25)
    inicio = int(input('QUE HORAS A PARTIDA COMEÇOU: '))
    print('==' * 25)
    fim = int(input('QUE HORAS A PARTIDA TERMINOU: '))
    calculo = inicio - fim
    if inicio < fim:
        calculo = fim - inicio
if inicio < fim:
    print(f'''SUA PARTIDA COMEÇOU AS {inicio}:00, E TERMINOU AS {fim}:00
    A PARTIDA DUROU EXATAMENTE {calculo}:00 .''')
else:
    print(f'''SUA PARTIDA COMEÇOU AS {fim}:00, E TERMINOU AS {inicio}:00
        A PARTIDA DUROU EXATAMENTE {calculo}:00 .''')
exit()

