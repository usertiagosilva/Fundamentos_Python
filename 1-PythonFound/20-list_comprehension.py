# 1 - Liste valores de 0 a 10 que sejam menos do que 4:

# Utilizando apenas o for:
for i in range(10):
    if i < 4:
        print(i)
        
# Utilizando a list comprehension (Lista de compressão):
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

print("\n____________________________________________\n")

# 2 - Jogos que possuam a letra a :
gamesList = ["Resident Evil 4", "Star wars Jedi Survivor", "Gta", "Homem Aranha"]
newlist = [x for x in gamesList if "a" in x]
print(newlist)

print("\n____________________________________________\n")

# 3 - Jogos que eu zerei
gamesFinished = [x for x in gamesList if x != "Gta"]
print(gamesFinished)
