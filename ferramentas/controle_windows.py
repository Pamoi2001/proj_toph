import os

def executar_comando(texto_ia):
    """
    Lê a resposta da Toph e procura por gatilhos de ação.
    Retorna True se executou algo, e False se for apenas conversa.
    """
    # A Toph decidiu abrir o Bloco de Notas
    if "[ABRIR_NOTEPAD]" in texto_ia:
        print(">> Sistema: A Toph forçou a abertura do Bloco de Notas...")
        os.system("notepad")
        return True
    
    # A Toph decidiu abrir a Calculadora
    elif "[ABRIR_CALCULADORA]" in texto_ia:
        print(">> Sistema: A Toph forçou a abertura da Calculadora...")
        os.system("calc")
        return True
        
    # A Toph decidiu abrir o Navegador
    elif "[PESQUISAR_GOOGLE]" in texto_ia:
        print(">> Sistema: A Toph forçou a abertura do Google Chrome...")
        os.system("start https://www.google.com")
        return True
        
    return False