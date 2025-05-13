from Passagem import *
 
if __name__ == "__main__":
    passagem = Passagem()
 
    passagem.cadastrarDadosPassageiro("João", "13 996452122", "45.652.250-45")
    passagem.cadastrarDadosPassagem("Ceará", "15/02/2025", "10:00", 5)
 
    passagem.mostrarDadosPassageiro()
    passagem.mostrarDadosPassagem()