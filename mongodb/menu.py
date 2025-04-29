from tkinter import *
from tkinter import ttk
import tkinter as tk
import subprocess
from PIL import Image, ImageTk
 
tela = Tk()
tela.title("Menu para Clientes")
tela.resizable(True,True)
tela.configure(background="#ffffff")

barra_menus = Menu(tela)
largura = 1000
altura = 700

def abrir_tela_clientes():
    subprocess.run(["python", "mongodbfirst.py"])

def abrir_tela_animais():
    subprocess.run(["python", "animais.py"])

def logout():
    tela.destroy()
    subprocess.run(["python", "login.py"])

menuarq = Menu(barra_menus)
menugestao = Menu(barra_menus)
opcoes_novo = Menu(menuarq)

barra_menus.add_cascade(label="Arquivo", menu=menuarq)
menuarq.add_cascade(label="Novo", menu=opcoes_novo)
menuarq.add_command(label="Abrir")
menuarq.add_command(label="Salvar")
menuarq.add_command(label="Salvar como...")
menuarq.add_separator()
menuarq.add_command(label="Sair", command=tela.quit)

opcoes_novo.add_command(label="Cadastrar")

barra_menus.add_cascade(label="Gestão", menu=menugestao)
menugestao.add_command(label="Animais", command=abrir_tela_animais)
menugestao.add_command(label="Clientes", command=abrir_tela_clientes)


#função para carregar e redimensionar imagens
def carregar_imagem(caminho, largura, altura):
    imagem = Image.open(caminho)
    imagem = imagem.resize((largura, altura))
    return ImageTk.PhotoImage(imagem)


imagem_fundo = carregar_imagem(r"icones\imagem_fundo.jpg", 1000, 700)

# imagem_pil = Image.open(caminho_imagem)
# largura, altura = imagem_pill.size
# if largura >800:
#     proporcao = largura / 2078
#     nova_altura = int(altura / proporcao)
#     imagem_pil = imagem_pil.resize((1024, nova_altura))
# imagem_tk = ImageTk.PhotoImage(imagem_pil)

lbl_imagem = Label(tela, image=imagem_fundo)
lbl_imagem.place(x=0,y=0)


# foto_sair = PhotoImage(file=r"icones\sair.png")
# foto_animais = PhotoImage(file = r"icones\logo_animais.png")
# foto_usuarios = PhotoImage(file = r"icones\logo_usuarios.png")
# foto_servicos = PhotoImage(file = r"icones\logo_servicos.png")
# foto_logout = PhotoImage(file = r"icones\logout.png")

foto_sair = carregar_imagem(r"icones\consultar.png", 100, 100)
foto_animais = carregar_imagem(r"icones\logo_animais.png", 100, 100)
foto_usuarios = carregar_imagem(r"icones\logo_usuarios.png", 100, 100)
foto_servicos = carregar_imagem(r"icones\logo_servicos.png", 100, 100)
foto_logout = carregar_imagem(r"icones\logout.png", 100, 100)


lbl_logo = Label(tela, text="PET SHOP DOGS", compound= TOP, image=foto_sair).place(x=890,y=580)
btn_animais = Button(tela, text="Animais", image=foto_animais, compound= TOP, command=abrir_tela_animais).place(x=100,y=200)
btn_clientes= Button(tela, text="Clientes", image=foto_usuarios, compound= TOP, command=abrir_tela_clientes).place(x=350,y=200)
btn_servicos = Button(tela, text="Serviços", image=foto_servicos, compound= TOP).place(x=550,y=200)
btn_logout = Button(tela, text="Logout", image=foto_logout, compound= TOP, command=logout).place(x=800,y=200)

tela.config(menu=barra_menus)


largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura,altura, posx, posy))
tela.mainloop()
#opcoes_novo.add_command(label="Salvar Imagem") // menu unico = add_command && // menu lista = add_cascade
#opcoes_novo.add_command(label="Pasta")




