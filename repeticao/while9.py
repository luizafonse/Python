nomes = ["Maria","Paulo","Joao", "Magali"]
localizar = input("Digite o nome a ser procurado: ")

for n in nomes:
    if n == localizar:
        print(f"O nome foi localizado: {n}")
        break
    else:
        print("O nome não foi localizado")