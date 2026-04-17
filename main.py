import os

def iniciar_toph():
    print("========================================")
    print("   SISTEMA TOPH INICIADO (Versão Alfa)  ")
    print("========================================\n")
    print("[+] Carregando Módulos de Memória... (Pendente)")
    print("[+] Carregando Sentidos... (Pendente)")
    print("[+] Conectando ao Motor IA... (Pendente)\n")
    
    print("Toph: Pode falar, novato. O que vamos hackear hoje?\n")
    
    while True:
        # Por enquanto vamos digitar, mas em breve isso será substituído pelo microfone
        comando = input("Você: ")
        
        if comando.lower() in ['sair', 'desligar', 'exit']:
            print("Toph: Finalmente. Vou voltar a dormir.")
            break
        
        # Aqui é onde vamos plugar a Toph respondendo ou executando ações no PC
        print(f"Toph: Eu ouvi você dizer '{comando}', mas minhas mãos e ouvidos ainda estão sendo programados.\n")

if __name__ == "__main__":
    iniciar_toph()