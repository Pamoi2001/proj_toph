import os
from ferramentas.controle_windows import executar_comando
from motor_ia.toph_cerebro import pensar_e_falar  # Importando a Rede Neural real!

def iniciar_toph():
    print("========================================")
    print("   SISTEMA TOPH INICIADO (Versão 1.0)   ")
    print("========================================\n")
    print("[+] Sentidos... (Pendente)")
    print("[+] Ferramentas do Sistema... [ONLINE]")
    print("[+] Motor IA (Deep Learning)... [ONLINE]\n")
    
    print("Toph: Motor neural ligado. Pode falar, novato. O que você quer fazer hoje?\n")
    
    while True:
        comando_usuario = input("Você: ")
        
        if comando_usuario.lower() in ['sair', 'desligar', 'exit']:
            print("Toph: Finalmente. Vou voltar a dormir.")
            break
        
        # --- O CÉREBRO REAL ENTRA EM AÇÃO ---
        print("\n[Toph está processando a resposta...]")
        resposta_toph = pensar_e_falar(comando_usuario)
        # ------------------------------------
        
        # 1. Limpamos as tags de sistema para a tela ficar imersiva
        texto_limpo = resposta_toph.replace("[ABRIR_NOTEPAD]", "").replace("[ABRIR_CALCULADORA]", "").strip()
        print(f"\nToph: {texto_limpo}\n")
        
        # 2. Enviamos o texto original (com a tag secreta, se houver) para o controlador do Windows
        executar_comando(resposta_toph)

if __name__ == "__main__":
    iniciar_toph()