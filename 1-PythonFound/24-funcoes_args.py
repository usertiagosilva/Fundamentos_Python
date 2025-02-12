"""
*args -  Utilizamos ele quando não temos certeza de quantos argumentos queremos ter em uma função 

**Kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento.
- Os argumentos são passados como um dicionário

"""
# 1 - Soma de números (Utilizando *args)
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n 
    print(f"A soma total é: \n {sum_total}")
    
sum(7)
sum(5, 5, 5)
sum(10, 15, 20, 10, 10)


# 2 - Apresentação de cursos (Utilizando **kwargs) 
def presentation(**data):
    print("\n📌 Curso:")
    for key, value in data.items():
        print(f"  {key.capitalize()}: {value}")

print("**** Lista de cursos ****")
presentation(name="Python", category="Backend", level="Iniciante")
presentation(name="Visão computacional com python", category="IA", level="Avançado")
presentation(name="Dashboards com dash", category="Data Science", level="Intermediário")


