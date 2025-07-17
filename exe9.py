
idade = int(input("Digite sua idade: "))
peso = int(input("Digite o seu peso (em Kg): "))
tatuagem = int(input("Digite se fez uma tatuagem no máximo no ano passado (Digite 1 para sim e 0 para não): "))
alcool = int(input("Digite se ingeriu álcool no máximo nas últimas 12 horas (Digite 1 para sim e 0 para não): "))

if idade >= 19 and idade <= 69 and peso >= 50 and tatuagem == 0 and alcool == 0:
    print("Você pode doar sangue!")
else:
    print("Você não pode doar sangue.")