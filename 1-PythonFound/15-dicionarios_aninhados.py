import pprint
gamesDict = {
    "resident evil 4" : {
        "yearLaunch" : 2023,
        "classification" : 9.8,
        "genre" : ["ação", "aventura"]
    },
    "mario" : {
        "yearLaunch" : 2017,
        "classification" : 10.0,
        "genre" : ["3D", "aventura"]
    },
    "donkey kong country" : {
        "yearLaunch" : 1995,
        "classification" : 9.5,
        "genre" : ["plataforma", "aventura"]
    }
}

#  Para imprimir objetos Python de uma maneira que mantém a estrutura clara e bem formatada
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informação dentro de um dicionario aninhado
print(gamesDict ["mario"]["genre"])

# 2 - Adicionar novo item
gamesDict["mario"] ["players"] = 1
print(gamesDict["mario"])

# 3 - Excluir um dicionario
del gamesDict["mario"]
pp.pprint(gamesDict)