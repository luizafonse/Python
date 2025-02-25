produto = 1
total = 0
i = 1
while produto != 0:
    produto = int(input(f"Produto {i}:"))
    total += produto
    i+=1
print(total)