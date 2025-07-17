saldo_disponivel = 1000
saldo_saque = int(input("Digite o valor a ser sacado: R$"))

if saldo_saque > saldo_disponivel:
    print(f'O seu saldo é insuficiente! Faltam R${saldo_saque - saldo_disponivel}')
else:
    print(f'Saque de R${saldo_saque} aprovado. Restam R${saldo_disponivel - saldo_saque}')
