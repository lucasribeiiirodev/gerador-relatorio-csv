from tkinter import filedialog, messagebox
import csv
 
def selecionar_arquivo():
    try:
        caminho_arquivo = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
 
        total_vendas = 0
        media_vendas = 0 
        produto_maisvendido = {}
        contador=0
        
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                total_vendas += int(linha["quantidade"])
                contador+=1
                if linha["produto"] in produto_maisvendido:
                    produto_maisvendido[linha["produto"]] += int(linha["quantidade"])
                else:
                    produto_maisvendido[linha["produto"]] = int(linha["quantidade"])
 
            media_vendas = total_vendas / contador
            
    except(FileNotFoundError, TypeError):
        messagebox.showerror(title="Erro:", message="Arquivo não encontrado!")
    
    if caminho_arquivo:
        return total_vendas, media_vendas, max(produto_maisvendido, key=produto_maisvendido.get), caminho_arquivo