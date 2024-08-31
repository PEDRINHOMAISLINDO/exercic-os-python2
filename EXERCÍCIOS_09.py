#9) Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

# REAJUSTE SALÁRIAL

print('=-' * 25)
print('REAJUSTE SALÁRIAL: ')
print('=-' * 25)
salario = float(input('INFORME SEU SALÁRIO: '))
porcentagem = float(input(' INFORME A PORCENTAGEM DE REAJUSTE: '))
resultado = (salario * porcentagem)/100
print(F'SEU SALÁRIO DE R${salario}, GANHOU {porcentagem}% DE AUMENTO . AGORA SEU SALÁRIO É DE R${resultado + salario:.2f}')


