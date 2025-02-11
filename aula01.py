# nome = "Maylon"
# idade = "29"

# print("Meu nome é " + nome+ " e tenho "+idade+" anos de idade.")


# primeiro_valor = int(input("Digite o primeiro valor: "))
# segundo_valor = int(input("Digite o segundo valor: "))

# resultado = primeiro_valor + segundo_valor

# print(resultado)


valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o valor do desconto em %: "))

valorDesconto = valorDesconto/100 * valorProduto
valorVenda = valorProduto - valorDesconto
print(f"O valor final da venda é: {valorVenda}")