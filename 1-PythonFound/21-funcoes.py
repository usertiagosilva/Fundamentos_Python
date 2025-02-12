# 1 - Função para imprimir Hello world:
def wellcome():
    print("Hello World")
wellcome()

print("________________________________________")

# 2 - Função para somar dois numeros:
def sum():
    #print(5 + 4)
    return 5 + 4
    
print(sum())

print("________________________________________")

# 3 - Função para cadastrar um jogo:
def create_game():
    name = input("Digite o nome do jogo: \n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo: \n"))
    gamePrice = float(input("Digite o preço do jogo: \n"))
    noteRating = float(input("Digite a nota de avaliação do jogo: \n"))
    
    print(f"{name} - R$ {gamePrice} - Ano de lançamento: {yearLaunch} - Avaliação {noteRating}")
    
create_game()
create_game()