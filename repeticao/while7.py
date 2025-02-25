import os
os.system('cls')

valor = 0.54
print("Panificadora tabela de preços")
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} - R${(valor * i):.2f}")