nomes = ["Luiz","Ana","Cristina","Fernanda","Maria Alice", "Joaquina"]
sair = 1
while sair !=0:
    localizar = input("Digite o nome a ser procurado: ")

    for n in nomes:
        if n == localizar:
            print(f"O nome foi localizado: {n}")
            break
    else:
            print("O nome não foi localizado")
            break
    sair = int(input("Digite: 1- Buscar e 0 - Sair"))