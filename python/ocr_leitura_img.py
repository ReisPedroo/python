import fitz
import re

def LeituraDocumento():
    caminhos = [
        r"caminho do arquivo pdf que voce ira ler",
        r"caminho do arquivo pdf que voce ira ler"
    ]
    for caminho in caminhos:
        pdf_document = fitz.open(caminho)
        page = pdf_document.load_page(0)
    
        # ajuste as coordenadas de acordo com o campo que voce quer pegar no arquivo
        coordenadas = fitz.Rect(500, 320, 565, 327)   
        text = page.get_text("text", clip=coordenadas)
    
        valor = re.sub(r'R\$|\s', '', text)
        print(valor)

LeituraDocumento()
