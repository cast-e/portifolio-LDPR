import math

km_l = float(input("Quantos Km/L faz o seu carro? "))
combustivel_l = float(input("Quantos L de combustível atualmente tem no seu carro? "))
preco_combustivel_l = 5.15
distancia_km = float(input("Quantos Km você irá percorrer (ida e volta)? "))
combustivel_ex = float(input("Quantos L a mais de combustível após o percurso? "))

litros_restantes = (distancia_km - (combustivel_l - combustivel_ex) * km_l)

if litros_restantes > 0:
    print(f"Você precisa abastecer: {round(litros_restantes * 10) / 10}L ou R${round(litros_restantes * preco_combustivel_l * 100) / 100}!")

    if combustivel_ex > 0:
        print(f"Ainda sobrando: {combustivel_ex}L, {combustivel_ex * km_l}Km ou R${combustivel_ex * preco_combustivel_l} (em combustível)")
else:
    print("Você não precisa abastecer.")
    print(f"Sobrará {-litros_restantes}L")

    percurso = math.floor(((combustivel_l - combustivel_ex) * km_l) / distancia_km)
    if percurso > 1:
        print(f"Você pode fazer o percurso {percurso} vezes!")