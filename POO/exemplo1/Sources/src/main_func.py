from Funcionario import *

if __name__ == '__main__':
    # func = Funcionario(5, "Afonso", 14000, True)
    # func2 = Funcionario(2, "Tarsila", 3000, True)
    # func3 = Funcionario(6, "Jeremias", 5000, True)

    # func.reajuste(10)
    # func2.reajuste(5)
    # func3.reajuste(15)
    # print(f"Salário do funcionário: {func.salario}")
    # print(f"Salário do funcionário 2: {func2.salario}")
    # print(f"Salário do funcionário 3: {func3.salario}")
    func = Funcionario(5, "Pedro", 2500, True)

    func.reajuste(10)

    print(f"Salário do(a) {func.getNome()}: {func.getSalario()} reais.")