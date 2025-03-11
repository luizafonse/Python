vetor = []
par = []
for i in range(5):
    numero = int(input(f"Digite o numero {i + 1}: "))
    vetor.append(numero)

print(f"Numeros: {vetor}")

for vet in vetor:
    if int(vet) % 2 == 0:
        par.append(vet)

print(f"Numeros: {par}")