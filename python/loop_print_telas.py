from PIL import Image
import fitz


pdf_document = fitz.open("caminho do pdf a ser printado")
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    
    # Converter a página em uma imagem
    pix = page.get_pixmap()
    pix.save(f"C:\\caminho do arquivo\\pagina_{page_number + 1}.png")
    image = Image.open(f"C:\\caminho do arquivo\\pagina_{page_number + 1}.png")