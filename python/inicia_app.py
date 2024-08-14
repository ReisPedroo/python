import subprocess
import re


def finalizar_processos(aplicativo):
    
    regex = r"[^\\]*$"
    if (str(re.search(regex, aplicativo)) != "None"):
        exe = re.search(regex, aplicativo)[0]

    subprocess.run(f"taskkill /f /im {exe}.exe")
        

def iniciar_aplicativo(aplicativo):
   
    # Iniciar o aplicativo
    subprocess.Popen(aplicativo)


aplicativo = "notepad"

print(aplicativo)

finalizar_processos(aplicativo)
iniciar_aplicativo(aplicativo)