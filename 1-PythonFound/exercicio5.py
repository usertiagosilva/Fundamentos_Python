# Verificação de letras maiúsculas e minúsculas:
def check_char(text):
    char_count = {"Uppercase": 0, "Lowercase": 0}
    for char in text:
        if char.isupper():
            char_count["Uppercase"] += 1
        elif char.islower():
            char_count["Lowercase"] += 1
    
    print("Texto original:\n", text)
    print("Número de letras maiúsculas:", char_count["Uppercase"])
    print("Número de letras minúsculas:", char_count["Lowercase"])

check_char("A melhor forma de Prever o Futuro é Criá-lo!")

# verífica números pares e ímpares:
def check_numbers(numbers):
    pairs = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            pairs.append(number)
        else:
            odd.append(number)
    return pairs, odd

# Solicita os números
user_input = input("Digite os números separados por espaço: ")

# Converte a entrada do usuário em uma lista de inteiros
numbers_list = list(map(int, user_input.split()))

# Chama a função com a lista digitada 
pares, impares = check_numbers(numbers_list)

# Exibe os resultados formatados
print("Números pares:", pares)
print("Números ímpares:", impares)

