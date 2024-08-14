from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service
import time
import subprocess

servico = Service(ChromeDriverManager().install())

def Navgator():

    max_tentativas = 5
    tentativa = 0

    while tentativa < max_tentativas:
        try: 
            subprocess.run("taskkill /f /im chrome.exe")
            navegador = webdriver.Chrome(service=servico)
            navegador.get('https://www.exemplo.com')
            time.sleep(2)
            navegador.maximize_window()

            navegador.find_element('xpath', 'xpath do campo a ser digitado')
            navegador.find_element('xpath', 'xpath do botao a ser clicado').click()

            time.sleep(3)

            navegador.find_element('xpath', 'xpath do campo a ser digitado"]').send_keys("")
            navegador.find_element('xpath', 'xpath do botao a ser clicado').click()

        except WebDriverException as e:
            print(f"ocorreu um erro: {e}")
            tentativa += 1
        except Exception as e:
            print(f"outro erro ocorreu: {e}")
            tentativa += 1
        finally:
            navegador.quit()

Navgator()