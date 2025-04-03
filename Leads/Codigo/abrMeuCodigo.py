import pandas as pd
import pyautogui as py
import clipboard
from time import sleep
import pyperclip
import apaga99linhas

for c in range(128):
    a = 1 # Valor do captcha para passar
    sleep(1)
    py.click(639,753) # Cliclar no Navegador
    sleep(2)
    py.press('f5') # Atualizar a pagina
    sleep(3.5)
    py.click(938,231) # Aperta em escolher o arquivo 
    sleep(3.5)
    py.click(347,192) # Apertou no arquivo
    sleep(3.5)
    py.click(509,445) # Abriu o arquivo
    sleep(3.5)
    py.click(499,281) # Apertou no Captha
    sleep(3.5)

    sleep(1)
    pyperclip.copy('')
    py.hotkey('ctrl','a') # Seleciona o capcha para ver se ele foi ativado, vendo se tem "Selecione" ou "select"
    py.hotkey('ctrl','c') # Copoou para ver o que tem
    select = clipboard.paste() # Recebe o que foi copiado
    sleep(3.5)
    if 'Selecione' in select or 'Select' in select:
        a = input("Captcha, sim?") # Se tiver o Captha ele ira para esse input para passar manualmente
        sleep(1)
        py.click(639,753) # Cliclar no Navegador
        sleep(1)

    py.click(735,345) # Botão Consultar
    sleep(5)
    py.moveTo(102,464) # primeira liniha
    sleep(1)
    py.mouseDown() # Apertou e segurou o mouse
    sleep(1)
    py.moveTo(1205,670) # Movendo o mouse para direita
    sleep(4)
    py.moveTo(1232,745) # Movendo o mouse para baixo
    sleep(3)
    py.moveTo(1250,673) # Movendo o mouse para a coluna para selecionar para jogar
    sleep(3)
    py.mouseUp() # Deixando o mouse parado
    sleep(0.3)
    py.hotkey('ctrl','c') # Copiando o que o mouse selecionou (Coluas e lihas)
    sleep(1)

    # Jogar no Excel as linhas e colunas
    py.click(718,745)
    sleep(3)
    py.press('esc')
    sleep(2)
    py.press('down')
    sleep(1)
    py.hotkey('ctrl','up')
    sleep(1)
    py.press('down')
    sleep(1)
    py.hotkey('ctrl','v')
    sleep(1)
    py.hotkey('ctrl','down')
    sleep(1)
    py.press('down')
    sleep(1)
    apaga99linhas.apagarLinhas() # Apagar as 99 linhas, 
    sleep(3)

