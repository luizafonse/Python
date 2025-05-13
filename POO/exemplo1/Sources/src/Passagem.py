class Passagem:
    def __init__(self, nomePassageiro="", telefone="", rg=None, localViagem=None, data=None, horario=None, numPoltrona=None):
        self.nomePassageiro = nomePassageiro
        self.telefone = telefone
        self.rg = rg
        self.localViagem = localViagem
        self.data = data
        self.horario = horario
        self.numPoltrona = numPoltrona
 
    def cadastrarDadosPassageiro(self, nomePassageiro, telefone, rg):
        self.nomePassageiro = nomePassageiro
        self.telefone = telefone
        self.rg = rg
 
    def cadastrarDadosPassagem(self, localViagem, data, horario, numPoltrona):
        self.localViagem = localViagem
        self.data = data
        self .horario = horario
        self.numPoltrona = numPoltrona
   
    def mostrarDadosPassageiro(self):
        print(f"O nome do passageiro é: {self.nomePassageiro}")
        print(f"O telefone do passageiro é: {self.telefone}")
        print(f"O RG do passageiro é: {self.rg}")
 
    def mostrarDadosPassagem(self):
        print(f"O local da viagem é: {self.localViagem}")
        print(f"A data da viagem é: {self.data}")
        print(f"O horário da viagem é: {self.horario}")
        print(f"O número da poltrona é: {self.numPoltrona}")