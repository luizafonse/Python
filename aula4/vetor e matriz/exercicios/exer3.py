matriz = []
for i in range(2):
    linha = []
    matriz.append(linha)
    for j in range(3):
        numero = input(f"Informe a cidade da posição ({i},{j}):")
        linha.append(numero)

for i in range(2):
    print(matriz[i])