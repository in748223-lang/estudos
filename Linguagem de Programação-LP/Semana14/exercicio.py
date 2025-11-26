#criar um pequeno sistema automatizado que mostre uma mensagem de alerta e confirmação para o usaário, paça informações básicas(nome e_email)confirme se o usário quer continuar, caso sim tire automaticamente uma captura de tela.

import pyautogui
import time

pyautogui.alert(text='Bem Vindo ao teste automatizado!',
               title='Inicio da automação',
               button='OK!')

nome=pyautogui.prompt (text='digite seu nome:',title='Informação obrigatoria!')
email=pyautogui.prompt(text='digite seu e-mail:',title='Informação obrigatoria!')


Resposta=pyautogui.confirm( 
    text=f'Confirme seus dados:\n\n nome: {nome}\n Email: {email}\n\n Deseja continuar com a captura de tela?',
    title='comfirmação de dados',
    buttons=['Sim', 'Não' , 'Cancelar']
    )

if Resposta =='Sim':
    pyautogui.alert('Prepare-se? A captura de tela será feita em três segundos',title='Captura de tela')
    time.sleep(3)
    pyautogui.screenshot (' Captura_usuário.png')
    pyautogui.alert('Captura realizada com sucesso!', title = 'Sucesso')

elif Resposta=='Não':
    pyautogui.alert('Processo cancela pelo usuário', title= 'Cancelado')

else:
    pyautogui.alert('A automação foi interrompida!', title= 'Encerrado')


    print(f'Nome: {nome}')
    print(f'Email: {email}')
    print(f'Resposta do usuario{Resposta}')







                       





