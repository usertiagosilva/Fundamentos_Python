# Entrada de dados:

name = input("Digite o nome do jogo: \n")
yearLauch = int(input("Digite o ano de lançamento do jogo:\n"))
classification = float(input("Digite a nota de classificação do jogo:\n"))

# Saída de dados:

if classification > 8.0 or yearLauch > 2015:
    print(f"o jogo {name} é bom. recomendo jogar!")
else:
    print(f"o jogo {name} ainda não atingiu uma boa nota. Por isso não recomendo!")