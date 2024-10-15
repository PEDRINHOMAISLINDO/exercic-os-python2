print('][' * 30)
print('APOSENTADORIA')
print('][' * 30)
idade = int(input('QUANTOS ANOS VOCÊ TEM: '))
print('][' * 30)
tempo_trabalhado = int(input('QUANTO ANOS VOCÊ TRABALHOU ( DIGITE SOMENTE OS NUMEROS ): '))
print('][' * 30)

if idade > 65 or tempo_trabalhado >= 30 or idade >= 60 and tempo_trabalhado >= 25:
    print('VOCÊ TEM DIREITO A SUA APOSENTADORIA')

else:
    print('VOCÊ NÃO TEM DIREITO À APOSENTADORIA')


