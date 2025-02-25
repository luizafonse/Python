import os
os.system('cls')

valor = 1.99
print("Loja tabela de preços")
for i in range(1, 51):
    print(f"{i} - R${(valor * i):.2f}")