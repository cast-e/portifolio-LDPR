altura_m = float(input("Digite sua altura em metros: "))
#peso_kg = float(input("Digite seu peso em kilogramas: "))

altura_cm = altura_m * 100

peso_base = altura_cm - 100

biotipo = input("Digite se você se acha do biotipo \"pequeno\", \"grande\" ou \"médio\": ")

if biotipo == "grande":
    peso_base *= 1.1
elif biotipo == "pequeno":
    peso_base *= 0.9

print(f"Seu peso ideal é {peso_base}")