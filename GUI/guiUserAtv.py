import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime
from PIL import Image, ImageTk

class ControlePessoas:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Pessoas")
        self.root.geometry("500x500")
        
        # Lista de cidades para o ComboBox
        self.cidades = ["Registro", "Miracatu", "Juquiá", "Cananéia", "Eldorado"]
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        ttk.Label(main_frame, text="Controle de Pessoas", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Código section
        ttk.Label(main_frame, text="Código:", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky=tk.W)
        
        # Nome and Idade
        nome_frame = ttk.Frame(main_frame)
        nome_frame.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Label(nome_frame, text="Nome:").pack(side=tk.LEFT)
        self.nome_entry = ttk.Entry(nome_frame, width=20)
        self.nome_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(nome_frame, text="Idade:").pack(side=tk.LEFT, padx=(10, 0))
        self.idade_entry = ttk.Entry(nome_frame, width=5)
        self.idade_entry.pack(side=tk.LEFT)
        
        # Sexo, Altura, Peso, Cidade
        sexo_frame = ttk.Frame(main_frame)
        sexo_frame.grid(row=3, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Label(sexo_frame, text="Sexo:").pack(side=tk.LEFT)
        self.sexo_var = tk.StringVar(value="M")
        ttk.Radiobutton(sexo_frame, text="M", variable=self.sexo_var, value="M").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(sexo_frame, text="F", variable=self.sexo_var, value="F").pack(side=tk.LEFT)
        
        ttk.Label(sexo_frame, text="Altura:").pack(side=tk.LEFT, padx=(10, 0))
        self.altura_entry = ttk.Entry(sexo_frame, width=5)
        self.altura_entry.pack(side=tk.LEFT)
        
        ttk.Label(sexo_frame, text="Peso:").pack(side=tk.LEFT, padx=(10, 0))
        self.peso_entry = ttk.Entry(sexo_frame, width=5)
        self.peso_entry.pack(side=tk.LEFT)
        
        ttk.Label(sexo_frame, text="Cidade:").pack(side=tk.LEFT, padx=(10, 0))
        self.cidade_combo = ttk.Combobox(sexo_frame, values=self.cidades, width=12)
        self.cidade_combo.pack(side=tk.LEFT)
        
        # Data Nascimento and Data Cadastro
        data_frame = ttk.Frame(main_frame)
        data_frame.grid(row=4, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Label(data_frame, text="Data Nascimento:").pack(side=tk.LEFT)
        self.nascimento_entry = ttk.Entry(data_frame, width=10)
        self.nascimento_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(data_frame, text="Data Cadastro:").pack(side=tk.LEFT, padx=(10, 0))
        self.cadastro_entry = ttk.Entry(data_frame, width=10)
        self.cadastro_entry.pack(side=tk.LEFT)
        
        # Data Atualização
        atualizacao_frame = ttk.Frame(main_frame)
        atualizacao_frame.grid(row=5, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Label(atualizacao_frame, text="Data Atualização:").pack(side=tk.LEFT)
        self.atualizacao_entry = ttk.Entry(atualizacao_frame, width=10)
        self.atualizacao_entry.pack(side=tk.LEFT)
        
        # Escolher imagem and Descrição
        imagem_frame = ttk.Frame(main_frame)
        imagem_frame.grid(row=6, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Label(imagem_frame, text="Escolher imagem:").pack(side=tk.LEFT)
        self.imagem_button = ttk.Button(imagem_frame, text="Selecionar", command=self.selecionar_imagem)
        self.imagem_button.pack(side=tk.LEFT, padx=5)
        
        descricao_frame = ttk.Frame(main_frame)
        descricao_frame.grid(row=7, column=0, columnspan=2, sticky=tk.W, pady=5)
        ttk.Label(descricao_frame, text="Descrição:").pack(side=tk.LEFT)
        self.descricao_text = tk.Text(descricao_frame, width=40, height=4)
        self.descricao_text.pack(side=tk.LEFT)
        
        # Buttons
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=8, column=0, columnspan=2, pady=15)
        
        ttk.Button(buttons_frame, text="Salvar", command=self.salvar).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Excluir", command=self.excluir).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Alterar", command=self.alterar).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Consultar", command=self.consultar).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Sair", command=self.root.quit).pack(side=tk.LEFT, padx=5)
        
        # Bottom section with person info
        bottom_frame = ttk.Frame(main_frame, borderwidth=1, relief=tk.SOLID)
        bottom_frame.grid(row=9, column=0, columnspan=2, sticky=tk.EW, pady=10)
        
        self.info_label = ttk.Label(bottom_frame, text="", font=('Arial', 10))
        self.info_label.pack(pady=5)
        
        # Separator
        ttk.Separator(main_frame, orient=tk.HORIZONTAL).grid(row=10, column=0, columnspan=2, sticky=tk.EW, pady=5)
        
        # Set default values
        self.set_default_values()
        
    def set_default_values(self):
        # Set some default values as shown in the image
        self.nome_entry.insert(0, "Luiz Claudio")
        self.idade_entry.insert(0, "22")
        self.sexo_var.set("M")
        self.altura_entry.insert(0, "1,65")
        self.peso_entry.insert(0, "50")
        self.cidade_combo.set("Registro")  # Set default city
        self.nascimento_entry.insert(0, "10-11-2000")
        self.cadastro_entry.insert(0, "10-11-2000")
        self.atualizacao_entry.insert(0, "10-11-2024")
        
    def selecionar_imagem(self):
        # Placeholder for image selection functionality
        messagebox.showinfo("Informação", "Funcionalidade de seleção de imagem será implementada aqui.")
        
    def salvar(self):
        # Placeholder for save functionality
        self.update_info_label()
        messagebox.showinfo("Informação", "Dados salvos com sucesso!")
        
    def excluir(self):
        # Placeholder for delete functionality
        messagebox.showinfo("Informação", "Funcionalidade de exclusão será implementada aqui.")
        
    def alterar(self):
        # Placeholder for update functionality
        messagebox.showinfo("Informação", "Funcionalidade de alteração será implementada aqui.")
        
    def consultar(self):
        # Placeholder for query functionality
        messagebox.showinfo("Informação", "Funcionalidade de consulta será implementada aqui.")
        
    def update_info_label(self):
        # Update the bottom info label with current data
        info_text = f"Código: Nome: {self.nome_entry.get()} | Idade: {self.idade_entry.get()} Sexo: {self.sexo_var.get().lower()}\n"
        info_text += f"Altura: {self.altura_entry.get()} Peso: {self.peso_entry.get()}\n"
        info_text += f"Cidade: {self.cidade_combo.get()} | Data Nasc: {self.nascimento_entry.get()}"
        
        self.info_label.config(text=info_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = ControlePessoas(root)
    root.mainloop()