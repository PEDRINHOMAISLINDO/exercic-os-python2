from colorama import init, Fore
init()
print('=-' * 25)
print('CONTA')
print('=-' * 25)
numero = input('DIGITE OS 6 NÚMEROS DE SUA CONTA: ')
print('=-' * 25)

if numero.isdigit() and len(numero) == 6:# VERIFICANDO SE "numero" É UM INTEIRO E SE OS CARACTÉRES DE "numero" É MAIOR QUE 6.
    print('SENHA VÁLIDA')

else:
    while numero.isdigit() and len(numero) != 6: # CASO CONTRÁRIO VAI CAIR NESSA ESTRUTURA DE REPETIÇÃO QUE PEDIRÁ NOVAMENTE O NÚMERO DA CONTA.
        print('SENHA INVÁLIDA')
        print('=-' * 25)
        numero = input('DIGITE O NÚMERO DE SUA CONTA: ')

saldo = float(input('DIGITE SEU SALDO DE CONTA: '))# PEDINDO MAIS INFORMAÇÕES.
debito = float(input('DIGITE SEU DÉBITO: '))#
credito = float(input('DIGITE SEU CRÉDITO: '))#
saldoatual = saldo - debito + credito # SOMA DAS INFORMAÇÕES.
if saldoatual > 0: # ESTRUTURA DE CONDIÇÃO.
    print(Fore.GREEN + f'SEU SALDO ESTÁ POSITIVO COM O VALOR DE R${saldoatual:.2f}')# SE A VARIÁVEL "saldoatual" FOR POSITIVA.
else:
    print(Fore.LIGHTRED_EX + f'SEU SALDO ESTÁ NEGATIVO! COM O VALOR DE R${saldoatual:.2f}')# SE A VARIÁVEL "saldoatual" FOR NEGATIVA.






