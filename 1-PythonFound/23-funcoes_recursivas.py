# É considerada recursiva quando dentro dela e feito uma ou mais chamadas a ela mesma

"""
Fatorial de um numero:
Exemplo
Numero 3 ->  3 * 2 * 1
Numero 5 ->  5 * 4 * 3* 2 * 1
"""

# 1 - Fatorial de um numero:
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))
    
number = int(input("Digite um numero para saber o Fatorial: \n"))
print(f"O fatorial de {number} é : \n {factorial(number)}")

# 2 - Soma total de um numero:
def soma(num):
    if num == 1:
        return 1
    else:
        return (num + soma(num - 1))
    
number = int(input("Digite um numero para saber a soma total: \n"))
print(f"A soma total de {number} é : \n {soma(number)}")
