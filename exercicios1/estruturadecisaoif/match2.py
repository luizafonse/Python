indice = int(input("Digite o número de acordo com o indice \nAção | Índice de Poluição \nConsiderar Aceitável | 0 até 2\nSuspender Atividades Grupo1 | 3 até 5 \nSuspender Atividades Grupo 1 e 2 |6 até 7 \nSuspender atividade de todos grupos |Acima de 8 \n"))

match indice:
    case 0|1|2:
        print("Aceitável")
    case 3|4|5:
        print("Suspender atividades do grupo 1 ")
    case 6|7:
        print("Suspender atividades grupos 1 e 2")
    case _:
        print("Suspender atividade de todos grupos")
