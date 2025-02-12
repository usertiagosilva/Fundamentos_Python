# Métodos para usar com as listas 

gameList = ["Resident Evil 4", "Star wars Jedi Survivor", "Gta", "Homem Aranha", "Mario World"]
print(gameList)

# 1- Contar tamanho da lista:
print(len(gameList))

# 2- Recuperar um item de uma lista pelo índice :
print(gameList.index("Gta"))

# 3- Adicionar item no final da lista:
gameList.append("Fast and Furious")
print(gameList)

# 4- Ordenar listas:
gameList.sort()
print(gameList)

# 5- Copiar os itens de uma lista para outra:
gameReset = gameList.copy()
gameReset.remove("Gta")
print(gameReset)

# 6- remover todos os itens da lista:
gameList.clear()
print(gameList)



