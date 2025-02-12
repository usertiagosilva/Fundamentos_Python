# Contagem regressiva lançamento do foguete:
# Módulo para gerar som
import winsound 

x = 10
while x >= 0:
    print(x)
    x -= 1 # x = x -1
# Beep para lançamento
winsound.Beep(2500, 1000)   
print("_____________________________________________________")

# Tabuada de um numero:
number = int(input("Tabuada do numero: \n"))
begin = int(input("De: \n"))
end = int(input("Até: \n"))

x = begin

while x <= end:
    print(f"Tabuada do {number} x {x} = {number * x}")
    x += 1
    