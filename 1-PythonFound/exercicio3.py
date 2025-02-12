# Cálculo da Distância e Preço da Passagem
distancia = float(input("Digite a distância que você quer percorrer em km:\n"))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.35

print(f"O valor da sua passagem é R$ {preco:.2f}")


# Cálculo de aumento salarial
salario = float(input("Digite o seu salário para calcular o aumento:\n"))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

print(f"Seu aumento será de R$ {aumento:.2f}, e seu novo salário será de R$ {novo_salario:.2f}.")