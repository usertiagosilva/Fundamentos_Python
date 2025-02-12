# Utilizando concatenação:

''' Jogoteca'''
# Entrada de dados
name = input("Digite o nome do jogo:\n")
yearLaunch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planIncluded = bool(input("Está incluso no serviço mensal?\n\n"))


print("### DADOS DO JOGO ###")
print("========================")
# Alternativa 1 :
# print("Nome do jogo:",name)
# print("Ano de lançamento do jogo:",yearLaunch)
# print("Preço do jogo:",gamePrice)
# print("Está incluido no plano?:",planIncluded)

# Alternativa 2 :
# print(" Nome do jogo:",name,"\n Ano de lançamento:",yearLaunch,"\n Preço do jogo:",gamePrice,"\n Esta incluido no plano:",planIncluded)

# Alternativa 3 :
print(f"Nome do jogo: {name} \nAno de lançamento: {yearLaunch} \nPreço do jogo: {gamePrice} \nEstá incluso no plano? {planIncluded}")
