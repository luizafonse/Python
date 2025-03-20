matriz = []

for i in range(5):
    linha = []
    for j in range(2):
        numero = int(input(f"Digite o número pra posição ({i}, {j}): "))
        linha.append(numero)
    matriz.append(linha)

print(" Matriz 5x2: ")
for linha in matriz:
    print(linha)