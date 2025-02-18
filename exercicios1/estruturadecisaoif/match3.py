print(5*"*", "CALCULO DE GRANDEZAS ELETRICAS", 5*"*")
print("1 - tensão em volts")
print("2 - corrente em amperes")
print("3 - resistência em ohms")
selec = int(input("Digite a opção"))
match selec:
    case 1:
        r = float(input("digite o valor da resistencia: "))
        i = float(input("digite o valor da corrente: "))
        u = r * i
        print(f"O valor da tensão em V é: {u}")
    case 2:
        r = float(input("digite o valor da resistencia: "))
        u = float(input("digite o valor da tensão: "))
        i = u / r
        print(f"O valor da corrente em A é: {i}")
    case 3:
        u = float(input("digite o valor da tensao: "))
        i = float(input("digite o valor da corrente: "))
        r = u / i
        print(f"O valor da resistencia em ohms é: {r}")

print(10*"*","FIM", 10*"*")