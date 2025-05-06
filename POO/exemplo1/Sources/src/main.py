from Pessoa import Pessoa

if __name__ == '__main__':
    # pessoa = Pessoa()

    # pessoa.mostrar_variavel_name()

    # print(f"variavel name: {__name__}")
    pessoa = Pessoa()
    pessoa.setNome("Afonso")
    pessoa.setIdade(18)
    pessoa.setAtivo(True)

    print(pessoa.getNome())
    print(pessoa.getIdade())
    print(pessoa.getAtivo())