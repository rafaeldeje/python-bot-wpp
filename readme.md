1. Descrição:

Este script em Python foi desenvolvido para automatizar o envio de mensagens no WhatsApp Web para uma lista de contatos predefinida. Utilizando a biblioteca pywhatkit, o script envia a mensagem especificada para cada contato na lista em intervalos regulares.

2. Funcionalidades:

Envio de Mensagens: O script utiliza a função pywhatkit.sendwhatmsg para enviar mensagens para os contatos listados.

Intervalo de Envio: Após o envio de cada mensagem, o script aguarda um intervalo de tempo (definido como 15 segundos no exemplo) antes de enviar a próxima mensagem.

Fechamento da Guia: Após o envio de todas as mensagens, o script utiliza pyautogui para fechar a guia do navegador ativa. Isso é feito pressionando as teclas Ctrl + W.

3. Configuração:

Contatos: A lista de contatos é definida na variável contatos. Adicione ou remova números de telefone conforme necessário.

Mensagem: A mensagem a ser enviada é especificada como o segundo argumento na função pywhatkit.sendwhatmsg. Modifique a string 'TESTE' para a mensagem desejada.

Intervalo de Envio: O tempo de espera entre o envio de mensagens é controlado pela função time.sleep. O valor padrão é 15 segundos, mas pode ser ajustado conforme necessário.

4. Execução:

Pré-requisitos: Certifique-se de ter as bibliotecas pywhatkit, keyboard, time, datetime, e pyautogui instaladas. Você pode instalá-las executando pip install pywhatkit keyboard pyautogui.

Execução: Execute o script Python e observe o envio automatizado de mensagens para os contatos especificados.

5. Observações:

Foco na Janela do Navegador: Certifique-se de que a guia do WhatsApp Web esteja ativa durante a execução do script. A automação pode ser sensível ao foco da janela.

Ajustes: Caso necessário, ajuste as coordenadas do clique do mouse utilizando pyautogui.click(x, y) para garantir que a guia do navegador esteja ativa antes de pressionar Ctrl + W.

Esperamos que este script facilite o envio automatizado de mensagens no WhatsApp Web. Sinta-se à vontade para personalizar conforme suas necessidades específicas.