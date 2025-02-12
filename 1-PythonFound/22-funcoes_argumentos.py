# 1 - Crie uma função que receba dois argumentos: Primeiro nome e segundo nome:
def full_name(fname, lname):
    print(f"Nome completo: \n {fname} {lname}")
    
full_name("Rodrigo", "Macedo")

# 2 - Crie uma função que some dois números via parâmetros:
def sum(a, b):
    return a + b

print(sum(10, 50))

# 3 - Argumentos default numa função:
def address(country = "Brasil"):
    print(f"E moro no {country}")
    
address()
address("Canada")

# 3 - Avaliação do jogo:
def rating_game(qtdrating):
    game_name = input("Digite o nome do jogo: \n")
    soma = 0
    for i in range(qtdrating):
        note = float(input("Digite uma nota para o jogo: \n"))
        soma += note
    print(f"A média de avaliação do jogo {game_name} é: {soma / qtdrating}")
    
rating = int(input("Digite quantas avaliações deseja fazer: \n"))
rating_game(rating)