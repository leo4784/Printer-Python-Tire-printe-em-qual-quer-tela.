import pyautogui
import time

# Aguarda 5 segundos
time.sleep(5)

# Captura a tela
screenshot = pyautogui.screenshot()

# Salva a captura como um arquivo
screenshot.save("print_tela.png")

print("Print da tela salvo como print_tela.png")
