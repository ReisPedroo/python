import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Informações de login
email_usuario = 'seu email'
email_senha = 'sua senha'

# Configuração do servidor SMTP
smtp_server = 'smtp.office365.com' # Servidor SMTP do seu e-mail (por exemplo, esse que é do Outlook)
smtp_port = 587 # pode usar a porta 25 tambem mas é recomendado usar a 587

# Informações do e-mail
email_destino = 'email de destino'
assunto = 'assunto do email'
corpo_html = '''
<html>
<head></head>
<body>
    <p>Olá!</p>
    <p>Este é um corpo de e-mail para teste.</p>
    <p>Grato.</p>
</body>
</html>
'''

# Criação do objeto de mensagem
msg = MIMEMultipart()
msg['From'] = email_usuario
msg['To'] = email_destino
msg['Subject'] = assunto

# Adicionando o corpo HTML
msg.attach(MIMEText(corpo_html, 'html'))

# Conexão com o servidor SMTP
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Inicia a conexão segura
    server.login(email_usuario, email_senha)
    text = msg.as_string()
    server.sendmail(email_usuario, email_destino, text)
    print('E-mail enviado com sucesso!')
except Exception as e:
    print(f'Erro ao enviar e-mail: {e}')
finally:
    server.quit()
