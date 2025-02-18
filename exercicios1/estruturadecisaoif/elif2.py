num = int(input("Digite o numero: "))

if num % 2 == 0:
    num *= num 
    print(f"O seu número é par, e seu quadrado é: {num}")
elif num % 2 != 0:
    num *=num * num
    print(f"O seu número é ímpar, e seu cubo é: {num}")