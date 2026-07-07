import tkinter as tk
from relatorios import selecionar_arquivo

def main():
 
    COR_FUNDO = "#F5F3EE"        
    COR_CARD = "#FFFFFF"
    COR_TEXTO_PRINCIPAL = "#2B2D2A"
    COR_TEXTO_SECUNDARIO = "#7A7A72"
    COR_ACCENT = "#2F6F4E"       
    COR_ACCENT_HOVER = "#255A3F"
    COR_BORDA = "#E2DFD6"
 
    FONTE_TITULO = ("Georgia", 18, "bold")
    FONTE_LABEL = ("Segoe UI", 10)
    FONTE_CAMINHO = ("Consolas", 9)
    FONTE_RESULTADO = ("Consolas", 11)
    FONTE_BOTAO = ("Segoe UI", 11, "bold")
 
    janela = tk.Tk()
    janela.title("Gerador de relatórios de vendas")
    janela.geometry('600x600')
    janela.configure(bg=COR_FUNDO)
    janela.resizable(False, False)
 
    frame_topo = tk.Frame(janela, bg=COR_FUNDO)
    frame_topo.pack(fill="x", padx=30, pady=(30, 10))
 
    tk.Label(
        frame_topo,
        text="Relatório de Vendas",
        font=FONTE_TITULO,
        bg=COR_FUNDO,
        fg=COR_TEXTO_PRINCIPAL
    ).pack(anchor="w")
 
    tk.Label(
        frame_topo,
        text="Selecione um arquivo CSV para gerar o resumo de vendas",
        font=FONTE_LABEL,
        bg=COR_FUNDO,
        fg=COR_TEXTO_SECUNDARIO
    ).pack(anchor="w", pady=(2, 0))
 
    def gerar_relatorio():
        try:
            total_vendas, media_vendas, produto_maisvendido, caminho_arquivo = selecionar_arquivo()
 
            texto_info.set(
                f"Total de vendas: {total_vendas}\n"
                f"Média de vendas: {media_vendas:.2f}\n"
                f"Produto mais vendido: {produto_maisvendido}"
            )
            texto_caminho.set(f"Arquivo selecionado: {caminho_arquivo}")
 
        except TypeError:
            texto_info.set("Selecione o arquivo para gerar o relatório: ")
            texto_caminho.set("")
 
    botao_selecionar = tk.Button(
        frame_topo,
        text="Selecionar arquivo CSV",
        command=gerar_relatorio,
        font=FONTE_BOTAO,
        bg=COR_ACCENT,
        fg="white",
        activebackground=COR_ACCENT_HOVER,
        activeforeground="white",
        relief="flat",
        borderwidth=0,
        padx=18,
        pady=8,
        cursor="hand2"
    )
    botao_selecionar.pack(anchor="w", pady=(16, 0))
 
    texto_caminho = tk.StringVar(value="")
    label_caminho = tk.Label(
        janela,
        textvariable=texto_caminho,
        font=FONTE_CAMINHO,
        bg=COR_FUNDO,
        fg=COR_TEXTO_SECUNDARIO,
        wraplength=540,
        justify="left"
    )
    label_caminho.pack(fill="x", padx=30, pady=(6, 0), anchor="w")
    
    frame_card = tk.Frame(
        janela,
        bg=COR_CARD,
        highlightbackground=COR_BORDA,
        highlightthickness=1
    )
    frame_card.pack(fill="both", expand=True, padx=30, pady=20)
 
    texto_info = tk.StringVar(value="Nenhum relatório gerado ainda.")
    label_info = tk.Label(
        frame_card,
        textvariable=texto_info,
        font=FONTE_RESULTADO,
        bg=COR_CARD,
        fg=COR_TEXTO_PRINCIPAL,
        justify="left",
        anchor="nw"
    )
    label_info.pack(fill="both", expand=True, padx=20, pady=20, anchor="nw")
 
    janela.mainloop()
 