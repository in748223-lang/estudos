import pyautogui
import time
pyautogui.alert(text = "simples iniciando a altomação", title="altomação de login",button="ok")
email = pyautogui.prompt (text = "digite seu email:", title= " informações obrigatorias")
print(f" seu email:{email}")
resposta=pyautogui.confirm (text="continuar rodando  essa informação?",title="confirmação",buttons=["sim","não","cancelar"])
print(resposta)
