import fitz
import re

def LeituraDocumento():
    caminhos = [
        r"nome do arquivo pdf que ira ler",
        r"nome do arquivo pdf que ira ler"
    ]
    for caminho in caminhos:
        pdf_document = fitz.open(caminho)
        page = pdf_document.load_page(0)
    
        coordenadas = fitz.Rect(500, 320, 565, 327)   
        text = page.get_text("text", clip=coordenadas)
    
        valor = re.sub(r'R\$|\s', '', text)
        print(valor)

LeituraDocumento()
