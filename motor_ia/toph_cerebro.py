# import torch
# from transformers import AutoTokenizer

# print("--- Inicializando o Motor Hugging Face da Toph ---\n")

# # 1. Escolhendo o modelo (Aqui você diz ao código qual "dicionário" baixar)
# modelo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
# print(f"Baixando e carregando o tokenizador do modelo: {modelo_id}...")

# # O AutoTokenizer é a classe mágica que se adapta a qualquer modelo do mundo
# tokenizador = AutoTokenizer.from_pretrained(modelo_id)

# # 2. O nosso texto de treinamento
# texto = "Você é a Toph, a maior dobradora de terra e sistemas do mundo! Pablo é um novato!"

# # 3. Codificando (Humano -> Máquina)
# # O transformers retorna um dicionário, nós queremos os 'input_ids' (os números)
# tokens = tokenizador(texto)["input_ids"]

# print(f"\nTexto original: '{texto}'")
# print(f"Quantidade de Tokens: {len(tokens)}")
# print(f"Como a rede neural enxerga: {tokens}")

# # 4. Decodificando (Máquina -> Humano)
# texto_recuperado = tokenizador.decode(tokens)
# print(f"\nTraduzindo de volta: '{texto_recuperado}'")

# # 5. Convertendo para Tensor (A munição do PyTorch)
# tensor_dados = torch.tensor(tokens, dtype=torch.long)
# print(f"\nFormato Tensor finalizado para o PyTorch:")
# print(tensor_dados)
import torch
import torch.nn as nn
import torch.nn.functional as F
from transformers import AutoTokenizer

print("--- Inicializando o Motor Hugging Face da Toph ---\n")

modelo_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizador = AutoTokenizer.from_pretrained(modelo_id)

texto = "Você é a Toph, a maior dobradora de terra e sistemas do mundo! Pablo é um novato."
tokens = tokenizador(texto)["input_ids"]
tensor_dados = torch.tensor(tokens, dtype=torch.long).unsqueeze(0) 

# Dimensões da nossa Rede Neural
tamanho_do_vocabulario = tokenizador.vocab_size 
dimensao_do_pensamento = 16 # Tamanho do Embedding

# 1. A Camada de Embedding (O Dicionário Matemático)
camada_embedding = nn.Embedding(num_embeddings=tamanho_do_vocabulario, embedding_dim=dimensao_do_pensamento)
vetores_espaciais = camada_embedding(tensor_dados)

print("--- Iniciando o Córtex Frontal (Self-Attention) ---")

# 2. Criando o Mecanismo de Atenção
class AttentionHead(nn.Module):
    def __init__(self, dimensao):
        super().__init__()
        # Criando as matrizes que vão gerar as Perguntas (Q), Chaves (K) e Valores (V)
        # O bias=False é padrão nessa arquitetura para manter a matemática limpa
        self.query = nn.Linear(dimensao, dimensao, bias=False)
        self.key   = nn.Linear(dimensao, dimensao, bias=False)
        self.value = nn.Linear(dimensao, dimensao, bias=False)

    def forward(self, x):
        # B = Batch (Quantas frases de uma vez = 1)
        # T = Time/Tokens (Quantas palavras = 28)
        # C = Channels/Dimensões (Coordenadas de cada palavra = 16)
        B, T, C = x.shape
        
        # Cada palavra gera seu Q, K e V
        q = self.query(x) # (B, T, C)
        k = self.key(x)   # (B, T, C)
        v = self.value(x) # (B, T, C)

        # 3. A Multiplicação (Q * K)
        # É aqui que as palavras conversam. Transpomos o K para a multiplicação de matrizes dar certo.
        # O resultado são as "Pontuações de Atenção" (quais palavras importam mais umas para as outras)
        pontuacoes = q @ k.transpose(-2, -1) 
        
        # Dividimos pela raiz quadrada da dimensão (para a matemática não explodir, regra do artigo do Google)
        pontuacoes = pontuacoes / (C ** 0.5) 
        
        # 4. O Softmax
        # Transforma as pontuações em porcentagens (de 0.0 a 1.0). 
        # Ex: "Toph" presta 90% de atenção em "dobradora" e 10% no resto.
        pesos = F.softmax(pontuacoes, dim=-1)

        # 5. A Síntese Final (Pesos * V)
        # Misturamos as porcentagens com o Valor real das palavras
        saida_contextualizada = pesos @ v
        
        return saida_contextualizada, pesos

# Instanciando o "Cérebro"
cabeca_de_atencao = AttentionHead(dimensao_do_pensamento)

# Passando os Embeddings pela Atenção
saida_final, matriz_de_pesos = cabeca_de_atencao(vetores_espaciais)

print(f"\nFormato de Entrada (Sem contexto): {vetores_espaciais.shape}")
print(f"Formato de Saída (Com contexto): {saida_final.shape}")

print("\n--- A Mágica Aconteceu ---")
print("Se você olhar o Formato de Saída, verá que os tensores têm o mesmo tamanho [1, 28, 16].")
print("Porém, os 16 números da saída AGORA contêm pedaços matemáticos das outras palavras da frase!")