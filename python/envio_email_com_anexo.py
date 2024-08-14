import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Informações de login
email_usuario = 'seu email'
email_senha = 'sua senha'

# Configuração do servidor SMTP
smtp_server = 'smtp.office365.com' #servidor smtp do seu email (por exemplo esse que é do outlook)
smtp_port = 587 # pode usar a porta 25 tambem mas é recomendado usar a 587

# Informações do e-mail
email_destino = 'email de destino'
assunto = 'assunto do email'
corpo_html = '''
<html>
<head></head>
<body>
    <p>Olá!</p>
    <p>Este é um corpo de email para teste.</p>
    <p>grato.</p>
</body>
</html>
'''

# Caminho do arquivo anexado
caminho_arquivo = 'caminho do anexo'

# Criação do objeto de mensagem
msg = MIMEMultipart()
msg['From'] = email_usuario
msg['To'] = email_destino
msg['Subject'] = assunto

# Adicionando o corpo HTML
msg.attach(MIMEText(corpo_html, 'html'))

# Anexando o arquivo
anexo = MIMEBase('application', 'octet-stream')
with open(caminho_arquivo, 'rb') as arquivo:
    anexo.set_payload(arquivo.read())

encoders.encode_base64(anexo)
anexo.add_header('Content-Disposition', f'attachment; filename={caminho_arquivo}')
msg.attach(anexo)

# Conexão com o servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_usuario, email_senha)
    text = msg.as_string()
    server.sendmail(email_usuario, email_destino, text)
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
finally:
    server.quit()
