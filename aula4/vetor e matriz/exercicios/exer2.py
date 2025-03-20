matriz = []
quantidade = 0
for i in range(4):
    linha = []
    matriz.append(linha)
    for j in range(4):
        numero = int(input(f"Digite o numero da posição ({i},{j}):"))
        linha.append(numero)
        if numero > 10:
            quantidade+=1

print(f"Quantidade de números maior que 10: {quantidade}")
for i in range(4):
    print(matriz[i])