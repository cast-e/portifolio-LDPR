ano = int(input("Digite o ano de fabricação do carro: "))
preco = float(input("Digite o preço de tabela do carro: R$"))

if ano < 2000:
    taxa = 1.0
else:
    taxa = 1.5

preco_final = preco + preco * (taxa / 100)

print(f'Preço com imposto aplicado: {preco_final}')
