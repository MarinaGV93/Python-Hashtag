import time
import pyautogui

time.sleep(5) # Pausa de 5 segundos para o usuário abrir a tela desejada

print(pyautogui.position()) # Imprime a posição do cursor

pyautogui.scroll(200) # Faz o scroll para baixo