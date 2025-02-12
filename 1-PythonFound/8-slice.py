#Fatiamento de string:

# Gerando Substrings a partir de uma String
gameName = "Fifa 23"
gameDescription = """
    Fifa 23 é um jogo de futebol 
    desenvolvido pela EA Sports e que 
    possibilita jogar localmente ou online.
"""

# Observação:  strings[inicio:fim] - indice começa na posição 0 || Indice final -1

# 1- Busque toda string a partir da primeira posição
print(gameName[0:])

# 2- Busque toda string até a ultima posição
print(gameName[:7])

# 3- Busque toda string da terceira até a ultima posição
print(gameName[2:])


"""
# Observação -> strings[inicio:fim:passo] - indice começa na posição 0 || Indice final -1
passo - Determina o incremento. por padrão esse numero é o 1.
"""

# 4- Busque toda a string de 2 em 2 caracteres 
print(gameName[::2])

# 5- Busque toda a string nos índices ímpares 
print(gameName[1::2])

# 6- Inverter uma string de trás pra frente 
print(gameName[::-1])
