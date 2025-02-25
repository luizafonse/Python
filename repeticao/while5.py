questao = 1
pontos = 0

while questao <= 3:
    resposta = input("Digite a resposta correta de A a D: ")
    if questao == 1 and resposta == "a":
        pontos +=1
    if questao == 2 and resposta == "c":
        pontos +=1
    if questao == 3 and resposta == "d":
        pontos +=1
    questao +=1
print(f"Você fez {pontos} pontos.")