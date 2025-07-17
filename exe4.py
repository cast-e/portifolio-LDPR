nome = input("Olá, qual é o seu nome? ")
forma_de_tratamento = input("Qual seria a sua forma de tratamento (Ex. senhor, senhora, estudante, etc)? ")

nome = nome.capitalize().strip()

if nome == "":
    nome = input("Por favor reescreva o seu nome. ")
    nome = nome.capitalize().strip()
    
elif nome == "Luís":
    print("VIXEEEEEEE!!!!")
    quit()

forma_de_tratamento = forma_de_tratamento.lower().strip()

if forma_de_tratamento == "":
    forma_de_tratamento = input("Por favor reescreva a sua forma de tratamento (Ex. senhor, senhora, estudante, etc). ")
    forma_de_tratamento = forma_de_tratamento.lower().strip()

elif forma_de_tratamento == "amigo":
    print(f"Não sou se amigo não hein {nome}.")
    quit()

print(f"Bom dia {forma_de_tratamento} {nome}!")