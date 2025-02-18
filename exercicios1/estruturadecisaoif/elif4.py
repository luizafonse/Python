num1 = float(input("Digite o primero numero: "))
num2 = float(input("Digite o segundo numero: "))

print("1 - media ponderada, pesos 2 e 3 respectivamente /n 2 - quadrado da soma dos doi num /n 3 - Cubo do menor num /n ")

op = int(input(" escolha uma opção de 1 a 3:"))

if op > 3 and op < 1:
    print("Opção inválida")
elif op == 1:
    media = (num1 * 2 + num2 * 3)/5
    print(f"Média ponderada calculada: {media:.2f}")

elif op == 2:
    quadrado = (num1 + num2) ** 2
    print(f"Quadrado da soma dos numeros: {quadrado:.2f}")

else:
    cubo = num2 ** 3
    print(f"{num2} é menor número, ele elevado ao cubo é: {cubo}")