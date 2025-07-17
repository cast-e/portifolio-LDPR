print('Classificador da competição de Capoeira')

nome = input('Digite o seu nome: ')
idade = int(input(f'{nome} digite a sua idade: '))

if idade <= 10:
    print('Classificação: Infantil')
elif idade <= 18:
    print('Classificação: Juvenil')
elif idade <= 30:
    print('Classificação: Adulta')
elif idade <= 10:
    print('Classificação: Sênior')
else:
    print('Idade inválida')
