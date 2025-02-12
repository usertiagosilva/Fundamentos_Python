gameSet = {"Fifa 24", "Pes 2020", "Crash", "Dragonball Z", "Mortal Kombat"}
print(gameSet)

# 1 - Buscar o tamanho do set
print(len(gameSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Fifa 23", True, 1, 90.30}
print(exampleSet)

# 3 - Adicionar item de outro set
gameSet.update(exampleSet)
print(gameSet)

# 4 - Remover um item no set
gameSet.remove(True)
print(gameSet)


# Não possibilita recuperar valores via fatiamento ou slice