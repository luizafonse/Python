sal = float(input("Digite o salário mensal: "))
perc = float(input("Digite o percentual de reajuste: "))

sal -= (sal*perc)/100

print(f"O salário reajustado fica {sal}")