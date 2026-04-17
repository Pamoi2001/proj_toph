import os
# Importando o módulo que acabamos de criar na outra pasta
from ferramentas.controle_windows import executar_comando

def iniciar_toph():
    print("========================================")
    print("   SISTEMA TOPH INICIADO (Versão Alfa)  ")
    print("========================================\n")
    print("[+] Carregando Sentidos... (Pendente)")
    print("[+] Conectando ao Motor IA... (Pendente)")
    print("[+] Ferramentas do Sistema... [ONLINE]\n")
    
    print("Toph: Pode falar, novato. O que você quer que eu faça?\n")
    
    while True:
        comando_usuario = input("Você: ")
        
        if comando_usuario.lower() in ['sair', 'desligar', 'exit']:
            print("Toph: Finalmente. Vou voltar a dormir.")
            break
        
        # --- SIMULAÇÃO DO CÉREBRO ---
        # No futuro, a resposta_toph virá daquela multiplicação de matrizes do toph_cerebro.py
        # Por enquanto, estamos forçando a resposta dela baseada na sua palavra-chave para testar o Windows
        
        resposta_toph = ""
        if "anotar" in comando_usuario.lower() or "bloco de notas" in comando_usuario.lower():
            resposta_toph = "Sério que você não consegue lembrar de nada sozinho? Tá bom, abrindo essa porcaria. [ABRIR_NOTEPAD]"
        
        elif "calculadora" in comando_usuario.lower() or "calcular" in comando_usuario.lower():
            resposta_toph = "Matemática básica é muito difícil pra você? Toma a calculadora. [ABRIR_CALCULADORA]"
            
        else:
            resposta_toph = "Para de balbuciar. Pede pra eu abrir a 'calculadora' ou um 'bloco de notas' para testarmos o sistema."

        # ------------------------------
        
        # 1. Limpamos a palavra secreta para a tela ficar bonita e parecendo mágica
        texto_limpo = resposta_toph.replace("[ABRIR_NOTEPAD]", "").replace("[ABRIR_CALCULADORA]", "").strip()
        print(f"\nToph: {texto_limpo}\n")
        
        # 2. Enviamos o texto original (com a palavra secreta) para o controlador do Windows
        executar_comando(resposta_toph)

if __name__ == "__main__":
    iniciar_toph()