import pywhatkit as kit  
import PySimpleGUI as sg  

sg.theme("topanga")  

layout = [  
    [sg.Text('Insira o número de telefone (formato internacional)')],  
    [sg.InputText('exemplo: +5511999999999', key='-NUM-')],  
    [sg.Text('Insira a mensagem')],  
    [sg.InputText('Sua mensagem aqui', key='-MSG-')],  
    [sg.Button('Enviar'), sg.Button('Sair')]  
]  

wind = sg.Window('Robô Rede Massa', layout)  

while True:  
    events, values = wind.read()  
    
    if events in (sg.WINDOW_CLOSED, 'Sair'):  
        break  
    
    if events == 'Enviar':  
        phone_number = values['-NUM-'] 
        message = values['-MSG-'] 

        
        import datetime  
        now = datetime.datetime.now()  
        send_hour = now.hour  
        send_minute = now.minute + 1  # Adiciona um minuto  

        # Envia a mensagem  
        kit.sendwhatmsg(phone_number, message, send_hour, send_minute)  

# Fechando a janela  
wind.close()  