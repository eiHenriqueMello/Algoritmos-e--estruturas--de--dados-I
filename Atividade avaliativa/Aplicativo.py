import tkinter as tk
from tkinter import messagebox
from Categoria import Categoria
from Desktop import Desktop
from Notbook import Notebook

class AplicativoCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Produtos")
        
       
        self.categorias = [
            Categoria(1, "Econômico"),
            Categoria(2, "Intermediário"),
            Categoria(3, "Premium")
        ]
        
        
        self.tipo_produto = tk.StringVar(value="desktop")
        self.modelo = tk.StringVar()
        self.cor = tk.StringVar()
        self.preco = tk.DoubleVar()
        self.categoria = tk.IntVar(value=1)
        self.potencia_fonte = tk.IntVar(value=500)
        self.tempo_bateria = tk.IntVar(value=5)
        
        
        self.criar_interface()
    
    def criar_interface(self):
        
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack()
        
       
        tk.Label(main_frame, text="Tipo de Produto:").grid(row=0, column=0, sticky="w")
        tk.Radiobutton(main_frame, text="Desktop", variable=self.tipo_produto, value="desktop").grid(row=0, column=1, sticky="w")
        tk.Radiobutton(main_frame, text="Notebook", variable=self.tipo_produto, value="notebook").grid(row=0, column=2, sticky="w")
        
       
        tk.Label(main_frame, text="Modelo:").grid(row=1, column=0, sticky="w")
        tk.Entry(main_frame, textvariable=self.modelo).grid(row=1, column=1, columnspan=2, sticky="ew")
        
        
        tk.Label(main_frame, text="Cor:").grid(row=2, column=0, sticky="w")
        tk.Entry(main_frame, textvariable=self.cor).grid(row=2, column=1, columnspan=2, sticky="ew")
        
       
        tk.Label(main_frame, text="Preço:").grid(row=3, column=0, sticky="w")
        tk.Entry(main_frame, textvariable=self.preco).grid(row=3, column=1, columnspan=2, sticky="ew")
        
      
        tk.Label(main_frame, text="Categoria:").grid(row=4, column=0, sticky="w")
        for i, categoria in enumerate(self.categorias):
            tk.Radiobutton(main_frame, text=categoria.nome, variable=self.categoria, value=categoria.id).grid(
                row=4, column=1+i, sticky="w")
        
        
        self.frame_especifico = tk.Frame(main_frame)
        self.frame_especifico.grid(row=5, column=0, columnspan=3, sticky="ew")
        
        self.atualizar_config_especifica()
        
        
        tk.Button(main_frame, text="Cadastrar", command=self.cadastrar_produto).grid(row=6, column=0, columnspan=3, pady=10)
        
        
        self.tipo_produto.trace_add("write", lambda *args: self.atualizar_config_especifica())
    
    def atualizar_config_especifica(self):
        
        for widget in self.frame_especifico.winfo_children():
            widget.destroy()
        
        if self.tipo_produto.get() == "desktop":
            tk.Label(self.frame_especifico, text="Potência da Fonte (W):").grid(row=0, column=0, sticky="w")
            tk.Entry(self.frame_especifico, textvariable=self.potencia_fonte).grid(row=0, column=1, sticky="ew")
        else:
            tk.Label(self.frame_especifico, text="Tempo de Bateria (h):").grid(row=0, column=0, sticky="w")
            tk.Entry(self.frame_especifico, textvariable=self.tempo_bateria).grid(row=0, column=1, sticky="ew")
    
    def cadastrar_produto(self):
        try:
        
            categoria_selecionada = None
            for cat in self.categorias:
                if cat.id == self.categoria.get():
                    categoria_selecionada = cat
                    break
            
            if self.tipo_produto.get() == "desktop":
                produto = Desktop(
                    modelo=self.modelo.get(),
                    cor=self.cor.get(),
                    preco=self.preco.get(),
                    categoria=categoria_selecionada,
                    potencia_da_fonte=self.potencia_fonte.get()
                )
            else:
                produto = Notebook(
                    modelo=self.modelo.get(),
                    cor=self.cor.get(),
                    preco=self.preco.get(),
                    categoria=categoria_selecionada,
                    tempo_de_bateria=self.tempo_bateria.get()
                )
            
          
            if produto.cadastrar():
                messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!\n\n" + 
                                  "\n".join([f"{k}: {v}" for k, v in produto.getInformacoes().items()]))
                self.limpar_campos()
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao cadastrar o produto:\n{str(e)}")
    
    def limpar_campos(self):
        self.modelo.set("")
        self.cor.set("")
        self.preco.set(0)
        self.categoria.set(1)
        self.potencia_fonte.set(500)
        self.tempo_bateria.set(5)

def main():
    root = tk.Tk()
    app = AplicativoCadastro(root)
    root.mainloop()

if __name__ == "__main__":
    main()