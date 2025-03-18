from tkinter import *

tela = Tk()

tela.title("Fatec de Registro")
tela.configure(background='#a2b3c4')
tela.geometry("480x320")
tela.resizable(True, True)
tela.maxsize(width=760, height=480)
tela.minsize(width=300, height=200)

# Corrigido: widgets Entry sem o uso de `.place()`, apenas com `.pack()`
txt_nome = Entry(tela, font="Arial 12 bold italic", fg="blue")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome: ")

txt_telefone = Entry(tela, font="Arial 12 bold italic", fg="green")
txt_telefone.pack()
txt_telefone.insert(0, "Digite o seu telefone: ")

txt_endereco = Entry(tela, font="Arial 12 bold italic", fg="red")
txt_endereco.pack()
txt_endereco.insert(0, "Digite o seu endereço: ")

txt_cpf = Entry(tela, font="Arial 12 bold italic", fg="yellow")
txt_cpf.pack()
txt_cpf.insert(0, "Digite o seu CPF: ")

# Função chamada ao clicar no botão
def clicar():
    # Obtendo o valor inserido nos campos de texto
    nome = txt_nome.get()
    telefone = txt_telefone.get()
    endereco = txt_endereco.get()
    cpf = txt_cpf.get()

    # Criando rótulos (labels) para exibir as informações coletadas
    lbl_nome = Label(tela, text="Bem-vindo " + nome)
    lbl_nome.pack()
    
    lbl_telefone = Label(tela, text="Telefone: " + telefone)
    lbl_telefone.pack()

    lbl_endereco = Label(tela, text="Endereço: " + endereco)
    lbl_endereco.pack()

    lbl_cpf = Label(tela, text="CPF: " + cpf)
    lbl_cpf.pack()

# Botão para acionar a função 'clicar'
btn_botao = Button(tela, text="Clique", command=clicar)
btn_botao.pack()

tela.mainloop()
