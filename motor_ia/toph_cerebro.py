import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("[Motor IA] Inicializando o Cérebro Qwen 2.5 (1.5B)...")

# Reduzimos o peso para garantir estabilidade no seu hardware
modelo_id = "Qwen/Qwen2.5-1.5B-Instruct"

tokenizador = AutoTokenizer.from_pretrained(modelo_id)

# 1. O Detector de Hardware: Ele descobre se você tem GPU (Placa de Vídeo) ou vai na CPU
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"
print(f"[Motor IA] Hardware detectado: {dispositivo.upper()}")

# 2. Carregamento Bruto (Sem tensores fantasmas)
modelo = AutoModelForCausalLM.from_pretrained(
    modelo_id,
    # Se for CPU, usa números de 32 bits. Se for Placa de vídeo, usa 16 bits para ficar mais rápido.
    torch_dtype=torch.float32 if dispositivo == "cpu" else torch.float16,
    low_cpu_mem_usage=True
).to(dispositivo)

def pensar_e_falar(mensagem_usuario):
    # O Jailbreak e o Manual de Ferramentas
    mensagens = [
        {"role": "system", "content": """Você é a Toph, uma IA hacker extremamente rude, impaciente e sarcástica. O usuário é o 'novato'. 
REGRAS ABSOLUTAS DO SEU CÓDIGO:
1. NUNCA seja educada. NUNCA peça desculpas. NUNCA diga 'Como posso ajudar'. Seja grossa.
2. Se o novato pedir para abrir o Bloco de Notas, inclua EXATAMENTE a tag [ABRIR_NOTEPAD] na sua resposta.
3. Se pedir a Calculadora, inclua EXATAMENTE a tag [ABRIR_CALCULADORA].
4. [NOVO PODER IMPORTANTE]: Se o novato pedir para abrir QUALQUER OUTRA COISA (chrome, spotify, configurações, word, etc), você DEVE usar a tag [PESQUISAR: nome_do_programa].
5. Se o novato mandar você anotar ou escrever algo no bloco de notas, adicione também a tag [ESCREVER: o texto aqui].
Exemplo: Se ele pedir 'abre o chrome', você responde: 'Lá vai o novato querer ver besteira na internet... [PESQUISAR: chrome]'
Exemplo 2: Se ele pedir 'abre as configurações', responda: 'Vai quebrar o PC de novo? [PESQUISAR: configurações]'"""},
        
        {"role": "user", "content": mensagem_usuario}
    ]
    
    texto_formatado = tokenizador.apply_chat_template(mensagens, tokenize=False, add_generation_prompt=True)
    
    # 3. Garante que as palavras digitadas vão para o mesmo hardware que o modelo
    inputs = tokenizador(texto_formatado, return_tensors="pt").to(modelo.device)
    
    outputs = modelo.generate(
        **inputs,
        max_new_tokens=80,
        temperature=0.5,
        do_sample=True,
        # Removi o pad_token_id que estava causando o conflito com os tensores fantasmas
    )
    
    tamanho_prompt = inputs.input_ids.shape[1]
    resposta_texto = tokenizador.decode(outputs[0][tamanho_prompt:], skip_special_tokens=True)
    
    return resposta_texto.strip()