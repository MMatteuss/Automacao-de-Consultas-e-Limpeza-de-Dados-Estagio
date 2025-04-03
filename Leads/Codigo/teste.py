import tkinter as tk
from tkinter import scrolledtext, messagebox, Toplevel
import pyperclip

class VivoFormatter:
    def __init__(self, root):
        self.root = root
        self.root.title("Formatador Vivo")
        self.root.geometry("900x700")
        self.root.configure(bg="white")
        
        # Cores Vivo (roxo)
        self.cor_vivo = "#660099"  # Roxo Vivo
        self.cor_texto = "black"
        self.cor_fundo = "white"
        
        self.setup_ui()
        
    def setup_ui(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg=self.cor_fundo)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Cabeçalho
        header_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            header_frame, 
            text="Vivo", 
            font=('Arial', 24, 'bold'), 
            fg=self.cor_vivo, 
            bg=self.cor_fundo
        ).pack(side=tk.LEFT)
        
        tk.Label(
            header_frame, 
            text="Formatador para Planilhas", 
            font=('Arial', 14), 
            fg=self.cor_texto, 
            bg=self.cor_fundo
        ).pack(side=tk.LEFT, padx=10)
        
        # Área de entrada
        input_frame = tk.LabelFrame(
            main_frame, 
            text=" COLE SEUS DADOS AQUI ",
            bg=self.cor_fundo,
            fg=self.cor_vivo,
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=10
        )
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        self.input_text = scrolledtext.ScrolledText(
            input_frame, 
            wrap=tk.WORD, 
            font=('Arial', 11), 
            height=15,
            padx=10,
            pady=10,
            bg=self.cor_fundo,
            fg=self.cor_texto,
            insertbackground=self.cor_vivo
        )
        self.input_text.pack(fill=tk.BOTH, expand=True)
        
        # Botões
        button_frame = tk.Frame(main_frame, bg=self.cor_fundo)
        button_frame.pack(fill=tk.X, pady=15)
        
        # Botão Enviar
        self.btn_gerar = tk.Button(
            button_frame,
            text="ENVIAR TEXTO",
            command=self.gerar_texto,
            bg=self.cor_vivo,
            fg="white",
            activebackground="#4a0068",
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=5,
            borderwidth=0
        )
        self.btn_gerar.pack(side=tk.LEFT, padx=5)
        
        # Botão Visualizar
        self.btn_visualizar = tk.Button(
            button_frame,
            text="VISUALIZAR",
            command=self.visualizar_texto,
            bg=self.cor_vivo,
            fg="white",
            state=tk.DISABLED,
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=5,
            borderwidth=0
        )
        self.btn_visualizar.pack(side=tk.LEFT, padx=5)
        
        # Botão Copiar
        self.btn_copiar = tk.Button(
            button_frame,
            text="COPIAR TEXTO",
            command=self.copiar_texto,
            bg=self.cor_vivo,
            fg="white",
            state=tk.DISABLED,
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=5,
            borderwidth=0
        )
        self.btn_copiar.pack(side=tk.LEFT, padx=5)
        
        # Barra de status
        self.status_bar = tk.Label(
            main_frame, 
            text="Pronto para formatar seus dados...", 
            bg=self.cor_fundo,
            fg=self.cor_texto,
            font=('Arial', 9),
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X, pady=(10, 0))
        
        # Efeito hover para botões
        self.setup_hover_effects()
    
    def setup_hover_effects(self):
        def on_enter(e):
            e.widget.config(bg="#4a0068")  # Roxo mais escuro
            
        def on_leave(e):
            e.widget.config(bg=self.cor_vivo)
            
        for btn in [self.btn_gerar, self.btn_visualizar, self.btn_copiar]:
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
    
    def gerar_texto(self):
        texto = self.input_text.get("1.0", tk.END).strip()
        
        if not texto:
            self.status_bar.config(text="Por favor, insira algum texto!", fg="red")
            return
            
        self.texto_copiar = f"""
Com base nesses dados:
"
{texto}
"
Quero que você me de: CNPJ, Razão Social, CEP, Logradouro (Como um endereço), Número (numero da casa), Complemento (As vezes não tem), Bairro, Cidade, UF, Telefone, E-mail e Consultor. Para mim colocar em uma planinha. Me de so os dados para mim colocar na planinha, fazendo com o que eu copie e cole na planinha, não precisando separar e copiar uma coisa por coisa, mas sim, copiar e colar na plainha. Caso você não encontre nenhum dado, quero que você coloque "Sem". Quero que fique um do lado do outro, nas outras colunas não na mesma coluna, sendo assim, ele iria pular de couluna, ficando mais facil de colar e jogar. Não precisa dizer oq vc fez, so os dados para mim colar.
""".strip()
        
        self.btn_visualizar.config(state=tk.NORMAL)
        self.btn_copiar.config(state=tk.NORMAL)
        self.status_bar.config(text="Texto formatado com sucesso!", fg="green")
    
    def visualizar_texto(self):
        janela = Toplevel(self.root)
        janela.title("Visualização - Vivo Formatter")
        janela.geometry("800x500")
        janela.configure(bg="white")
        
        # Centralizar janela
        self.center_window(janela)
        
        # Frame de visualização
        frame = tk.LabelFrame(
            janela,
            text=" TEXTO FORMATADO ",
            bg="white",
            fg=self.cor_vivo,
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Área de texto
        texto = scrolledtext.ScrolledText(
            frame,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg="white",
            fg="black",
            padx=10,
            pady=10
        )
        texto.pack(fill=tk.BOTH, expand=True)
        texto.insert(tk.END, self.texto_copiar)
        texto.config(state=tk.DISABLED)
        
        # Botão Copiar
        btn = tk.Button(
            janela,
            text="COPIAR TEXTO",
            command=lambda: self.copiar_texto(janela),
            bg=self.cor_vivo,
            fg="white",
            font=('Arial', 10, 'bold'),
            padx=20,
            pady=5,
            borderwidth=0
        )
        btn.pack(pady=10)
        
        # Efeito hover
        btn.bind("<Enter>", lambda e: e.widget.config(bg="#4a0068"))
        btn.bind("<Leave>", lambda e: e.widget.config(bg=self.cor_vivo))
    
    def copiar_texto(self, janela=None):
        pyperclip.copy(self.texto_copiar)
        self.status_bar.config(text="Texto copiado para área de transferência!", fg="green")
        if janela:
            janela.destroy()
    
    def center_window(self, window):
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'+{x}+{y}')

if __name__ == "__main__":
    root = tk.Tk()
    app = VivoFormatter(root)
    root.mainloop()