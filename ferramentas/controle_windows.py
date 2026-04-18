import os
import time
import pyautogui

def executar_comando(texto_ia):
    """Lê a resposta da Toph e executa as ações no Windows."""
    
# [NOVO] Abrir Bloco de Notas e ditar texto dinâmico!
    if "[ABRIR_NOTEPAD]" in texto_ia:
        print(">> Sistema: A Toph forçou a abertura do Bloco de Notas...")
        os.system("notepad")
        time.sleep(1) # Espera o notepad abrir
        
        # Procura se a Toph colocou a tag [ESCREVER: ...]
        if "[ESCREVER:" in texto_ia:
            inicio = texto_ia.find("[ESCREVER:") + 10
            fim = texto_ia.find("]", inicio)
            texto_para_digitar = texto_ia[inicio:fim].strip()
            pyautogui.write(texto_para_digitar, interval=0.05)
        else:
            pyautogui.write("O que eu devo anotar, novato?", interval=0.05)
            
        return True
    
    # Abrir Calculadora
    elif "[ABRIR_CALCULADORA]" in texto_ia:
        print(">> Sistema: A Toph forçou a abertura da Calculadora...")
        os.system("calc")
        return True
        
    # [NOVO PODER] - Abrir QUALQUER coisa
    # Se ela colocar [PESQUISAR: chrome] ou [PESQUISAR: spotify]
    elif "[PESQUISAR:" in texto_ia:
        # Pega a palavra que vem depois do dois pontos
        inicio = texto_ia.find("[PESQUISAR:") + 11
        fim = texto_ia.find("]", inicio)
        programa = texto_ia[inicio:fim].strip()
        
        print(f">> Sistema: A Toph apertou a tecla Windows e buscou por '{programa}'...")
        pyautogui.press('win') # Aperta a tecla Windows
        time.sleep(0.5)
        pyautogui.write(programa, interval=0.05) # Digita o nome do programa
        time.sleep(0.5)
        pyautogui.press('enter') # Aperta Enter
        return True
        
    return False