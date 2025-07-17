nome = input('Digite o seu nome: ')
codigo = int(input(f'Olá {nome}! Digite o código do seu cargo: '))

cargo = ""
percentual = 0

if codigo == 101:
    percentual = 10
    cargo = 'Gerente'
elif codigo == 102:
    percentual = 20
    cargo = 'Engenheiro'
elif codigo == 103:
    percentual = 30
    cargo = 'Técnico'
else:
    print("Erro! Código Inválido!")
    exit(1)

print(f'Seu cargo é {cargo} e seu percentual adicional é de {percentual}%!')

salario_antigo = float(input('Digite seu salário atual: R$'))
print(f'Seu salário antigo é: R${salario_antigo:.2f}.')

salario_novo = salario_antigo * (1 + percentual / 100)

print(f'Seu salário novo é: R${salario_novo:.2f}')
print(f'A diferença entre seu salario novo e seu antigo é de: R${salario_novo - salario_antigo:.2f}')

exit(0)