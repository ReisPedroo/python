from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

navegador.get('www.exemplo.com')
time.sleep(5)
navegador.maximize_window()


try: 
    navegador.find_element('xpath', 'xpath do campo a ser digitado').send_keys("")
    navegador.find_element('xpath', 'xpath do botao a ser clicado').click()

    time.sleep(3)

    navegador.find_element('xpath', 'xpath do campo a ser digitado"]').send_keys("")
    navegador.find_element('xpath', 'xpath do botao a ser clicado').click()
    pass
except:
    pass

