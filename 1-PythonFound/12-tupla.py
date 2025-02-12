# Tupla tem que estar dentro do parentese, separado por virgula.
gamesTuple = ("Fifa23", "Red Dead 2", "Gta V", "Spiderman", "Mario")
print(gamesTuple)

# Verificar o tipo da variável.
print(type(gamesTuple))

# 1 - Buscar os dois primeiros itens da tupla
print(gamesTuple[:2])

# 2 - Buscar o ultimo item da lista
print(gamesTuple[-1])

# 3 - Buscar jogos até uma determinada posição
print(gamesTuple[:3])

# 4 - Buscar jogos de uma posição em diante
print(gamesTuple[3:])

# 5 - Recuperar um item da tupla pelo indice
print(gamesTuple.index("Gta V"))


# - Não possibilita adicionar valores na tupla
# - Não possibilita remover valores na tupla
# - Não possibilita ordenar valores na tupla