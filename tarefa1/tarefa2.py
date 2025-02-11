valor =float(input("Digite o valor da prestação: "))
tax = float(input("Digite o valor em porcentagem da taxa: "))
temp = float(input("Digite os meses de atraso: "))

atraso = valor + (valor*(tax/100)*temp)

print(f"O valor do atraso é {atraso}")