# Também conhecida como anônima, pode receber qualquer numero, porém somente uma unica expressão.

# 1 - Função de potência de numero
power = lambda num: num **2

# 2 - Função que verifica se um numero é par
pair = lambda x: x % 2 == 0

# 3 - Função que divide um numero por outro
divNum = lambda x, y: x / y

# 4 - Função que inverte uma string
reverse = lambda s: s[:: -1]

print(power(5))
print(power(9))
print(pair(25))
print(pair(30))
print(divNum(10, 2))
print(divNum(6, 2))
print(reverse("Python"))
print(reverse("Gabriellen"))


