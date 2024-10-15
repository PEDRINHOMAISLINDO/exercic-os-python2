senha_usuario = 9999
codigo_usuario = 1234
print('**' * 25)
print('CÓDIGO DO USUÁRIO')
print('**' * 25)
codigo = int(input('DIGITE O CÓDIGO DO USUÁRIO: '))
print('**' * 25)

while codigo != codigo_usuario:
    print('''CÓDIGO DE USUÁRIO INCORRETO!
    DIGITE NOVAMENTE!''')
    print('**' * 25)
    codigo = int(input('DIGITE O CÓDIGO DO USUÁRIO: '))
    print('**' * 25)

senha = int(input('DIGITE A SENHA DO USUÁRIO: '))
print('**' * 25)

while senha != senha_usuario:
    print('''SENHA DE USUÁRIO INCORRETA!
    DIGITE A SENHA NOVAMENTE!''')
    print('**' * 25)
    senha = int(input('DIGITE A SENHA DO USUÁRIO: '))
    print('**' * 25)

print('ACESSO PERMITIDO...')
exit()


