class Funcionario:
    def __init__(self, codigo, nome, salario, situacao):
        self.codigo = codigo
        self.nome = nome
        self.__salario = salario
        self.situacao = situacao


    def getSalario(self):
        return self.__salario
    def setSalario(self, salario):
        self.__salario = salario

    def getNome(self):
        return self.nome
    def setSalario(self, nome):
        self.nome = nome

    def reajuste(self, valor):
        # self.salario *= 1 + (valor / 100)
        self.__salario += (self.__salario * valor / 100)