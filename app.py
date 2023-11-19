import pywhatkit
import time
from datetime import datetime
import pyautogui

#2 Definir para quais contatos iremos enviar as mensagens
contatos = ['+xxxxxxxxxxxxx']

#3 Definir intervalo de envio
while len(contatos) >= 1:
    # Enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Teste 1', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    
    # Aguardar um tempo para a mensagem ser enviada
    time.sleep(15)
    
    # Fechar a guia do navegador usando pyautogui
    pyautogui.hotkey('ctrl', 'w')

#4 Testar!
