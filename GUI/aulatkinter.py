from tkinter import *

tela = Tk()

tela.title("Fatec de Registro")
tela.configure(background='#a2b3c4')
tela.geometry("480x320")
tela.resizable(True, True)
tela.maxsize(width=760, height=480)
tela.minsize(width=300, height=200)

lbl_nome = Label(tela, text="Nome: ", font="Arial 12 bold italic", fg="blue").place (x=10, y=10)
lbl_telefone = Label(tela, text="Telefone: ", font="Arial 12 bold italic", fg="green").place (x=10, y=40)
lbl_endereço = Label(tela, text="Endereço: ", font="Arial 12 bold italic", fg="red").place (x=10, y=70)
lbl_cpf = Label(tela, text="CPF: ", font="Arial 12 bold italic", fg="yellow").place (x=10, y=100)

btn_botao = Button(tela, text="Clicar")
btn_botao.pack()

tela.mainloop()