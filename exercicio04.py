nome = input("Olá, qual é o seu nome? ")
forma_de_tratamento = input("Qual seria a sua forma de tratamento (Ex. senhor, senhora, estudante, etc)? ")

nome = nome.capitalize().strip()

if nome == "":
    nome = input("Por favor reescreva o seu nome. ")
    nome = nome.capitalize().strip()

forma_de_tratamento = forma_de_tratamento.lower().strip()

if forma_de_tratamento == "":
    forma_de_tratamento = input("Por favor reescreva a sua forma de tratamento (Ex. senhor, senhora, estudante, etc). ")
    forma_de_tratamento = forma_de_tratamento.lower().strip()

print(f"Bom dia {forma_de_tratamento} {nome}!")
