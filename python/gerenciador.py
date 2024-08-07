import subprocess
import os

def rodar_script(nome_script):
    try:
        # mudar onde esta escrito 'codigos' para o nome da pasta onde estao os scripts
        resultado = subprocess.run(['python', os.path.join('codigos', nome_script)], capture_output=True, text=True)
        print(resultado.stdout)
    except Exception as e:
        print(f"erro ao rodar {nome_script}: {e}")

def main():
    #colocar o nome dos scripts que estao dentro da sua pasta como no exemplo a baixo
    scripts = ['test1.py', 'test2.py', 'test3.py']

    for script in scripts:
        rodar_script(script)

if __name__ == "__main__":
    main()


# os codigos que forem rodar pelo gerenciador precisam estar no formato a baixo cada um em um arquivo
'''

def main():
    print("test1.py rodando")
  
if __name__ == "__main__":
    main()

'''
