print('<>' * 25)
print('DESCRIÇÃO DE UM PRODUTO')
print('<>' * 25)
produto = input('DIGITE O NOME DO SEU PRODUTO: ').upper() # DEIXANDO A LETRA MAIÚSCULA COM O ATRIBUTO upper()
print('<>' * 25)
quantidade_produto = int(input(f'QUANTIDADE DE {produto}: '))
print('<>' * 25)
preco_unitario = float(input(f'QUANTO CUSTA UMA UNIDADE DE {produto}: '))
print('<>' * 25)
total_produto = quantidade_produto * preco_unitario

if quantidade_produto <= 5: # ESTRUTURA DE CONDIÇÃO SE A QUANTIDADE DO SEU PRODUTO FOR MENOR OU IGUAL A 5
    desconto2 = total_produto - (total_produto * 0.02)
    print(f'VOCÊ RECEBEU UM DESCONTO DE 2%, ENTÃO O PREÇO DO SEU PRODUTO FICOU R${desconto2:.2f}')
    print('<>' * 25)

elif quantidade_produto > 5 and quantidade_produto <= 10: # ESTRUTURA DE CONDIÇÃO SE A QUANTIDADE DO SEU PRODUTO FOR MAIOR QUE 5 E MENOR QUE 10
    desconto3 = total_produto - (total_produto * 0.03)
    print(f'VOCÊ RECEBEU UM DESCONTO DE 3%, ENTÃO O PREÇO DO SEU PRODUTO FICOU R${desconto3:.2f}')
    print('<>' * 25)

elif quantidade_produto > 10: # ESTRUTURA DE CONDIÇÃO SE A QUANTIDADE DO SEU PRODUTO FOR MAIOR QUE 10
    desconto5 = total_produto - (total_produto * 0.05)
    print(f'VOCÊ RECEBEU UM DESCONTO DE 5%, ENTÃO O PREÇO DO SEU PRODUTO FICOU R${desconto5:.2f}')
    print('<>' * 25)
exit()