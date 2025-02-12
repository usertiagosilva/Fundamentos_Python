# exemplo de for com range
for i in range(5):
    print("hellow World")
print("__________________________________________")

gamesList =  ["Resident Evil 4", "Star wars Jedi Survivor", "Gta", "Homem Aranha"]

# 1 - Iterando valores de uma lista:
for game in gamesList:
    print(game)
print("_________________________________________")

# 2 - Quando a condição for atendida, o loop sera encerrado:
for game in gamesList:
    if game == "Gta":
        break
    print(game)
print("__________________________________________")

# 3 - Quando a condição for atendida, o loop vai para a próxima iteração:
for game in gamesList:
    if game == "Star wars Jedi Survivor":
        continue
    print(game)
print("__________________________________________")

# 4 - Avaliação de jogos
gameName = input("Digite o nome do jogo:\n")
gameRating = int (input("Digite quantas avaliações deseja fazer no jogo:\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo;\n"))
    sum += note # equivale a sum = sum + note
print(f"Média de avaliação do jogo {gameName} é {sum/gameRating :.2f}")




    


