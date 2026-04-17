import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("[Motor IA] Acordando a Toph (Carregando Pesos Neurais)...")

# 1. Carregando o Tokenizador e o Modelo
modelo_id = "Qwen/Qwen2.5-1.5B-Instruct"
tokenizador = AutoTokenizer.from_pretrained(modelo_id)

# ATENÇÃO: Na primeira vez que rodar, isso vai baixar uns 2GB de "inteligência" (os pesos da rede neural).
modelo = AutoModelForCausalLM.from_pretrained(modelo_id, device_map="auto")

def pensar_e_falar(mensagem_usuario):
    """
    Função que recebe o texto do usuário, passa pela rede neural e cospe a resposta da Toph.
    """
    # 2. O DNA da Toph (O Prompt de Sistema formatado para o TinyLlama)
    prompt = f"""<|system|>
Você é a Toph, uma assistente de sistema durona, sarcástica e confiante. Você foi criada pelo Pablo, mas o chama de 'novato'. 
Suas regras:
- Responda em Português de forma curta e direta.
- Se o usuário pedir para abrir o Bloco de Notas, inclua a exata tag [ABRIR_NOTEPAD] no final da sua frase.
- Se o usuário pedir para calcular algo ou abrir a calculadora, inclua a exata tag [ABRIR_CALCULADORA] no final.</s>
<|user|>
{mensagem_usuario}</s>
<|assistant|>
"""
    
    # 3. Tokenizando (Humano -> Máquina)
    inputs = tokenizador(prompt, return_tensors="pt")
    
    # 4. A Mágica da Inferência (Loop Autoregressivo)
    outputs = modelo.generate(
        **inputs, 
        max_new_tokens=70,  # Limita o tamanho da resposta para ela não falar demais
        temperature=1,    # Dá um toque de criatividade e sarcasmo
        do_sample=True,
        pad_token_id=tokenizador.eos_token_id # Evita avisos de erro no terminal
    )
    
    # 5. Decodificando (Máquina -> Humano)
    # Precisamos cortar o prompt original para ela não repetir tudo que dissemos
    tamanho_prompt = inputs.input_ids.shape[1]
    resposta_tokens = outputs[0][tamanho_prompt:]
    resposta_texto = tokenizador.decode(resposta_tokens, skip_special_tokens=True)
    
    return resposta_texto.strip()

# Pequeno teste local (só roda se você executar esse arquivo diretamente)
if __name__ == "__main__":
    print(pensar_e_falar("Toph, abre a calculadora aí pra mim."))