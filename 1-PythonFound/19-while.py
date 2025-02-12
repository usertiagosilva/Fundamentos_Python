# Avaliação dos jogos utilizando while
gameName = input("Digite o nome do jogo:\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0

while(rating != -1):
    rating = float(input("Informe a nota do jogo:\n"))
    if(rating != -1):
        totalRating += rating # totalRating = totalRating  + rating
        qtdRating += 1 # qtdRating = qtdrating + 1
        average = totalRating / qtdRating
print(f"Media das avaliações do jogo {gameName} é {average:.2f}") 