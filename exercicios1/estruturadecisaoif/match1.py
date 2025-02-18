letra = input("Digite uma letra: ")

match letra.lower():
    case "a"|"e"|"i"|"o"|"u":
        print("voce digitou uma vogal")
    case _:
        print("voce digitou uma consoante")

