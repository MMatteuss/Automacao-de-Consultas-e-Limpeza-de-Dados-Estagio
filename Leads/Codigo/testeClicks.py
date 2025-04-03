import pandas as pd
import pyautogui as py
import clipboard
from time import sleep
import pyperclip
import apaga99linhas

"""
Script automatizado para consultas repetidas em um sistema web com tratamento de captcha.
Cada iteração:
1. Atualiza a página
2. Seleciona arquivo
3. Verifica/resolve captcha (se necessário)
4. Executa consulta
5. Copia resultados
6. Cola no Excel
7. Limpa linhas desnecessárias
8. Salva o arquivo Excel

Tempos reduzidos ao mínimo viável para operação estável.
"""

# Configuração de segurança do PyAutoGUI
py.PAUSE = 0.5  # Pequena pausa entre cada comando do pyautogui
py.FAILSAFE = True  # Permite abortar movendo mouse para canto superior esquerdo

for c in range(128):
    captcha_value = 1  # Valor padrão para bypass de captcha
    
    # 1. Preparação inicial
    sleep(0.5)
    py.click(639, 753)  # Foca no navegador
    sleep(1.5)
    
    # 2. Atualizar página
    py.press('f5')
    sleep(2.5)  # Tempo reduzido mas suficiente para carregamento
    
    # 3. Selecionar arquivo
    py.click(938, 231)  # Botão 'escolher arquivo'
    sleep(1.5)
    py.click(347, 192)  # Seleciona arquivo na janela
    sleep(1.5)
    py.click(509, 445)  # Confirma seleção
    sleep(1.5)
    py.click(499, 281)  # Clica no campo captcha
    
    # 4. Verificar captcha AUTOMATICAMENTE
    max_tentativas = 999  # Número máximo de tentativas
    captcha_detectado = False
    
    for _ in range(max_tentativas):
        sleep(0.3)
        py.hotkey('ctrl', 'a')
        sleep(0.2)
        py.hotkey('ctrl', 'c')
        sleep(0.3)
        select = clipboard.paste()
        
        if 'Selecione' in select or 'Select' in select:
            captcha_detectado = True
            sleep(0.5)  # Espera 0.5s antes de tentar novamente
        else:
            captcha_detectado = False
            break
    
    if captcha_detectado:
        captcha_value = input("Captcha detectado! Digite o valor: ")
        py.click(639, 753)  # Retorna ao navegador
        sleep(0.5)
    
    # 5. Executar consulta
    py.click(735, 345)  # Botão Consultar
    sleep(3)  # Tempo crítico - manter suficiente para processamento
    
    # 6. Copiar resultados - Versão otimizada mas confiável
    py.click(735, 345)  # Botão Consultar
    sleep(3.5)  # Tempo suficiente para a consulta processar (reduzido de 5s)
    
    # Seleção inteligente com tempos ajustados
    py.moveTo(102, 464)  # Posição inicial (primeira linha)
    sleep(0.5)  # Tempo reduzido mas seguro para estabilização
    
    py.mouseDown()  # Inicia seleção
    sleep(0.3)  # Pequena pausa para garantir que iniciou
    
    # Movimento horizontal rápido mas controlado
    py.moveTo(1205, 670, duration=1.2)  # Reduzido de 4s para movimento
    sleep(0.5)  # Pausa estratégica após movimento horizontal
    
    # Movimento vertical otimizado
    py.moveTo(1232, 745, duration=1.5)  # Reduzido de 3s
    sleep(2)  # Pequena estabilização
    
    # Ajuste final mais rápido
    py.moveTo(1250, 673, duration=0.8)  # Reduzido de 3s
    sleep(0.3)  # Última estabilização antes de soltar
    
    py.mouseUp()  # Finaliza seleção
    sleep(0.3)  # Garante que soltou antes de copiar
    
    py.hotkey('ctrl', 'c')  # Copia seleção
    sleep(0.7)  # Tempo suficiente para copiar (reduzido de 1s)
    
    # 7. Colar no Excel e limpar
    py.click(696,741)  # Foca no Excel
    sleep(1)
    py.press('esc')
    sleep(0.5)
    py.press('down')
    py.hotkey('ctrl', 'up')
    sleep(0.3)
    py.press('down')
    sleep(0.3)
    py.hotkey('ctrl', 'v')  # Cola dados
    sleep(0.5)
    py.hotkey('ctrl', 'down')
    sleep(0.3)
    py.press('down')
    sleep(0.3)
    py.click(738,30) # Salvar
    sleep(1)
    
    # 8. Limpeza de linhas
    apaga99linhas.apagarLinhas()
    sleep(1)  # Tempo para finalizar processamento
    
    # 9. Salvar arquivo Excel (NOVO)
    py.hotkey('ctrl', 's')  # Salva o arquivo
    sleep(1.5)  # Tempo para o salvamento