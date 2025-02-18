alt1 = float(input("digite a primeira altura: "))
alt2 = float(input("digite a segunda altura: "))
alt3 = float(input("digite a terceira altura: "))

if alt1 > alt2 and alt1 > alt3:
    maior = alt1
    if alt2 > alt3:
        meio = alt2
        menor = alt3
    else:
        meio = alt3
        menor = alt2


elif alt2 > alt1 and alt2 > alt3:
    maior = alt2
    if alt1 > alt3:
        meio = alt1
        menor = alt3
    else:
        meio = alt3
        menor = alt1
else: 
    maior = alt3
    if alt1 > alt2:
        meio = alt1
        menor = alt2
    else:
        meio = alt2
        menor = alt1

print(f"A maior altura é {maior} a do meio é {meio} e a menor é {menor}")