class Pessoa:
    # def mostrar_variavel_name(self):
    #     print(f'variavel nome da pessoa: {__name__}')

    def __init__(self, nome="Sem nome", idade=0, ativo=False):#valores padrao caso nao tenha input na main
        self.nome = nome
        self.idade = idade
        self.ativo = ativo

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getIdade(self):
        return self.idade

    def setIdade(self, idade):
        self.idade = idade

    def getAtivo(self):
        return self.ativo

    def setAtivo(self, ativo):
        self.ativo = ativo

    def ativar(self):
        self.ativo = True
        print("A pessoa foi ativada")

    def desativar(self):
        self.ativo = False
        print("A pessoa foi desativada")