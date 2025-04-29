from tkinter import *
from tkinter import messagebox
import subprocess
import pymongo
 
# screen = tela
screen = Tk()
screen.title("Acesso ao Sistema")
screen.geometry("400x200")
screen.resizable(False, False)
# width e height igual a largura e altura
width = 400
height = 200

cliente = pymongo.MongoClient("mongodb://localhost:27017")
db = cliente['exemplo']
cliente = db['login']
 
def sair():
    resposta = messagebox.askquestion("Sair do Sistema ?", "Você tem certeza que deseja sair?")
    if resposta == 'yes':
        screen.destroy()
def validar_acesso(usuario, senha):
    resultado = cliente.find_one({"usuario":usuario, "senha": senha})
    if usuario == 'admin' and senha == '123':
        abrir_app()
    else:
        messagebox.showerror("erro de Login", "Usuário ou senha incorretos.")
def abrir_app():
    screen.destroy()
    # Trocar index.py para o nome da sua outra tela
    subprocess.run(["python", "menu.py"])
def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario, senha)#sera chamada no botao passando parametro usuario e senha

lbl_usuario = Label(screen, text="Usuário").place(x=50, y=60)
lbl_senha = Label(screen, text="Senha").place(x=50, y=100)
txt_senha = Entry(screen, width=20, show="*")
txt_senha.place(x=100, y=100)
txt_usuario = Entry(screen,width=20)
txt_usuario.place(x=100,y=60)

foto_acesso = PhotoImage(file=r"icones\acesso.png")
foto_sair = PhotoImage(file=r"icones\sair.png")
btn_usuario = Button(screen, text="Acessar", image= foto_acesso, compound= TOP, command=click_botao).place(x=250,y=50)
btn_sair = Button(screen, text="Sair", image= foto_sair, compound= TOP, command=sair).place(x=320,y=50)

largura_screen = screen.winfo_screenwidth()
altura_screen = screen.winfo_screenheight()
posx = largura_screen/2 - width/2
posy = altura_screen/2 - height/2
print(largura_screen, altura_screen)
screen.geometry("%dx%d+%d+%d" % (width,height, posx, posy))
screen.mainloop()